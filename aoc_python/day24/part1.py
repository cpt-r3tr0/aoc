
def solve_puzzle_p1(filename):
    with open(filename, "r") as f:
        grid = list(map(str.strip, f.readlines()))
    pass

if __name__ == "__main__":
    filename = "example.txt"
    print(f'Solution for example file is : {solve_puzzle_p1(filename)}')
    filename = "day16_input.txt"
    print(f'Solution for my file is : {solve_puzzle_p1(filename)}')