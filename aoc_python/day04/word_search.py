
def word_search(filename) -> int:
    word_grid = []
    with open(filename) as file:
        for line in file:
            word_grid.append(list(line.strip()))
    count_of_xmas = 0
    rows = len(word_grid)
    cols = len(word_grid[0])
    target = 'XMAS'
    reverse_target = 'SAMX'
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1), (0,1),
        (1,-1), (1,0), (1,1)
    ]

    for i in range(rows):
        for j in range(cols):
            if word_grid[i][j] == 'X':
                for di, dj in directions:
                    if foundXMAS(word_grid, i, j, di, dj, target):
                        count_of_xmas += 1
                    if foundXMAS(word_grid, i, j, di, dj, reverse_target):
                        count_of_xmas += 1

    return count_of_xmas

def foundXMAS(word_grid, i, j, di, dj, target):
    if (i + 3*di < 0 or i + 3*di >= len(word_grid) 
        or
        j + 3*dj < 0 or j + 3*dj >= len(word_grid[0])):
        return False
    for k in range(4):
        current_row = i + k*di
        current_col = j + k*dj
        if word_grid[current_row][current_col] != target[k]:
            return False
    return True

filename = 'day4_input.txt'
result = word_search(filename)
print(f'Result: {result}')