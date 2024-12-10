from collections import defaultdict
from itertools import combinations

def t_frequencies(filename):
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
    
    dx, dy = bx - ax, by - ay

    i = 0
    while True:
        if in_bounds(ax - dx * i, ay - dy * i, n):
            yield (ax - dx * i, ay - dy * i)
        else:
            break
        i += 1
    
    i = 0
    while True:
        if in_bounds(bx + dx * i, by + dy * i, n):
            yield (bx + dx * i, by + dy * i)
        else:
            break
        i += 1


if __name__ == "__main__":
    print(f'Day 08 part 2 : {t_frequencies("./day08_input.txt")}')