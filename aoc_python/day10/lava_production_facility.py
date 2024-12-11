
def find_reachable_nines(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    reachable_nines = set()
    
    def is_valid(x, y, current_height):
        return (0 <= x < rows and 
                0 <= y < cols and 
                grid[x][y] == current_height + 1)
    
    def dfs(x, y, current_height, visited):
        if current_height == 9:
            reachable_nines.add((x, y))
            return
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            next_x, next_y = x + dx, y + dy
            if (next_x, next_y) not in visited and is_valid(next_x, next_y, current_height):
                visited.add((next_x, next_y))
                dfs(next_x, next_y, current_height + 1, visited)
                visited.remove((next_x, next_y))
    
    visited = {(start_x, start_y)}
    dfs(start_x, start_y, 0, visited)
    return len(reachable_nines)

def solve_hiking_trails(grid):
    rows, cols = len(grid), len(grid[0])
    total_score = 0
    
    # Find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                score = find_reachable_nines(grid, i, j)
                total_score += score
                
    return total_score

def read_grid_from_file(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            # Convert each character to integer and add as row
            row = [int(char) for char in line.strip()]
            grid.append(row)
    return grid


def main():
    grid = read_grid_from_file('day10_input.txt')
    result = solve_hiking_trails(grid)
    print(f"Sum of trailhead scores: {result}")

if __name__ == "__main__":
    main()