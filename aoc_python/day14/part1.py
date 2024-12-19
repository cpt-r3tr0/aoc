import math
import re


def safey_score(robots: list[tuple[int]], width, height) -> int:
    q = [0] * 4
    for xf, yf in robots:
        midw, midh = width // 2, height // 2
        if xf < midw:
            if yf < midh:
                q[0] += 1
            if yf > midh:
                q[1] += 1
        elif xf > midw:
            if yf < midh:
                q[2] += 1
            if yf > midh:
                q[3] += 1
    return math.prod(q)




def solve_puzzle_p1(filename, width=11, height=7) -> int:
    lines = []  
    with open(filename, "r") as f:
        lines = list(map(str.strip, f.readlines()))

    robots = []
    for line in lines:
        # p=0,4 v=3,-3
        x, y, dx, dy = tuple(map(int, re.findall(r"-?\d+", line)))
        robots.append((x, y, dx, dy))

    robots_filtered = []
    for x, y, dx, dy in robots:
        xf = (x + (dx * 100)) % width
        yf = (y + (dy * 100)) % height
        robots_filtered.append((xf, yf))
    
    return safey_score(robots_filtered, width, height)


if __name__ == "__main__":
    filename = "example.txt"
    print(f'Solution for example file is : {solve_puzzle_p1(filename)}')
    filename = "day14_input.txt"
    print(f'Solution for my file is : {solve_puzzle_p1(filename, 101, 103)}')