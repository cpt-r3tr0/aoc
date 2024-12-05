def count_xmas_patterns(filename) -> int:
    # Read the grid
    with open(filename, 'r') as file:
        grid = file.read().strip().split('\n')
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += has_xmas(grid, i, j)
            
    return count


def has_xmas(grid, i, j) -> bool:
    n = len(grid)
    m = len(grid[0])
    
    # Check bounds and center A
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    if grid[i][j] != "A":
        return False
    
    # Check both diagonals
    diag_1 = f"{grid[i-1][j-1]}{grid[i+1][j+1]}"  # Top-left to bottom-right
    diag_2 = f"{grid[i-1][j+1]}{grid[i+1][j-1]}"  # Top-right to bottom-left
    
    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]


print(f'Result: {count_xmas_patterns("day4_input.txt")}')