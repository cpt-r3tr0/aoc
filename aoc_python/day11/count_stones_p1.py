from functools import cache

@cache
def count_stones(val: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    if val == 0:
        return count_stones(1, blinks - 1)
    str_val = str(val)
    len_str_val = len(str_val)
    if len_str_val % 2 == 0:
        return count_stones(
            int(str_val[: len_str_val // 2]), blinks - 1
        ) + count_stones(int(str_val[len_str_val // 2 :]), blinks - 1)
    return count_stones(val * 2024, blinks - 1)



def main(filename) -> None:
    stones = []
    with open(filename) as file:
        stones = list(map(int, file.read().strip().split(" ")))
    print(sum(count_stones(s, 25) for s in stones))


if __name__ == "__main__":
    main("day11_input.txt")