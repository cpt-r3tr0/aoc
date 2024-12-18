import re


def solve_puzzle(puzzle: str, offset: int = 0) -> tuple[int]:
    a1, a2 = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", puzzle)[0]))
    c1 += offset
    c2 += offset

    # https://en.wikipedia.org/wiki/Cramer%27s_rule
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

    if int(x) == x and int(y) == y:
        return tuple(map(int, (x, y)))
    return (0, 0)


def solve_puzzle_p1(filename: str) -> int:
    with open(filename, "r") as f:
        puzzles = f.read().split("\n\n")

    part1 = 0
    for puzzle in puzzles:
        a, b = solve_puzzle(puzzle)
        part1 += a * 3 + b
    return part1

# part1 = 0
# part2 = 0
# for puzzle in puzzles:
#     a, b = solve_puzzle(puzzle)
#     part1 += a * 3 + b
#     a2, b2 = solve_puzzle(puzzle, offset=10000000000000)
#     part2 += a2 * 3 + b2

# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")


if __name__ == "__main__":
    filename = "example.txt"
    print(f'Solution for example file is : {solve_puzzle_p1(filename)}')
    filename = "day13_input.txt"
    print(f'Solution for my file is : {solve_puzzle_p1(filename)}')