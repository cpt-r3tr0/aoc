from collections import defaultdict
from itertools import combinations

def resonant_collinearity(filename):
    with open (filename) as fin:
        grid = fin.read().strip().split("\n")

    n = len(grid)

    antinodes = set()

    all_locs = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i, j))
    
    for freq in all_locs:
        locs = all_locs[freq]
        for a, b in combinations(locs, r=2):
            for antinode in get_antinodes(a, b, n):
                antinodes.add(antinode)

    return len(antinodes)


def in_bounds(x,y,n):
    return 0 <= x < n and 0 <= y < n
    

def get_antinodes(a,b,n ):
    ax, ay = a
    bx, by = b
    
    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)

    if in_bounds(cx, cy, n):
        yield (cx, cy)
    if in_bounds(dx, dy, n):
        yield (dx, dy)


if __name__ == "__main__":
    print(f'Day 08 part 1 : {resonant_collinearity("./day08_input.txt")}')