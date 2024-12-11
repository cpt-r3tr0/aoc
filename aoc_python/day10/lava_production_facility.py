
def lava_production_faciltiy(filename)-> int:
    grid =[]
    with open (filename) as file:
        data = file.read().splitlines()
        for line in data:
            grid.append([int(char) for char in line]) 
    n = len(grid)
   
    for i in range(0, n):
        for j in range(0,n):
            if grid[i][j] == 0:
                find_trail(grid, i, j)
    return count

def find_trail(grid, x, y ):
    n = len(grid)
    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    print(f'x: {x}, y: {y}')
    for i in range (0,n):
        for j in range(0,n):
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if isvalid(new_x, n) and isvalid(new_y, n):
                    if grid[new_x][new_y] - grid[x][y] == 1:
                        print(f'value at new_x: {new_x}, new_y: {new_y} is {grid[new_x][new_y]}')

    return count

def isvalid(x, n):
    return x >= 0 and x < n

if __name__ == "__main__":
    filename = "example.txt"
    filename2 = "day10_input.txt"
    print(f'The total paths for example are : {lava_production_faciltiy(filename)}')
    # print(f'The total paths input are : {lava_production_faciltiy(filename2)}')