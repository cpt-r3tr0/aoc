def count_distinct_paths(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    path_count = 0
    
    def is_valid(x, y, current_height):
        return (0 <= x < rows and 
                0 <= y < cols and 
                grid[x][y] == current_height + 1)
    
    def dfs(x, y, current_height, visited):
        nonlocal path_count
        if current_height == 9:
            path_count += 1
            return
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            next_x, next_y = x + dx, y + dy
            if (next_x, next_y) not in visited and is_valid(next_x, next_y, current_height):
                visited.add((next_x, next_y))
                dfs(next_x, next_y, current_height + 1, visited)
                visited.remove((next_x, next_y))
    
    visited = {(start_x, start_y)}
    dfs(start_x, start_y, 0, visited)
    return path_count

def solve_hiking_trails_part2(grid):
    rows, cols = len(grid), len(grid[0])
    total_rating = 0
    
    # Find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                rating = count_distinct_paths(grid, i, j)
                total_rating += rating
                
    return total_rating

def read_grid_from_file(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(char) for char in line.strip()]
            grid.append(row)
    return grid

def main():
    grid = read_grid_from_file('day10_input.txt')
    result = solve_hiking_trails_part2(grid)
    print(f"Sum of trailhead ratings: {result}")

if __name__ == "__main__":
    main()
