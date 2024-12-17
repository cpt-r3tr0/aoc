from collections import deque

def perimeter(region: set[tuple[int]]) -> int:
    total = 0
    for r, c in region:
        num_neighbors = len(
            [
                1
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
                if (r + dr, c + dc) in region
            ]
        )
        total += 4 - num_neighbors
    return total


def calculate_perimeter(filename: str) -> int :
    grid = []
    with open(filename, "r") as f:
        grid = list(map(str.strip, f.readlines()))
    num_rows = len(grid)
    num_cols = len(grid[0])

    regions = []
    seen = set()
    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) in seen:
                continue
            region = set()
            queue = deque([(r, c)])
            while queue:
                rr, cc = queue.popleft()
                region.add((rr, cc))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = rr + dr, cc + dc
                    if (
                        (nr, nc) not in seen
                        and 0 <= nr < num_rows
                        and 0 <= nc < num_cols
                        and grid[nr][nc] == grid[rr][cc]
                    ):
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            regions.append(region)

        total_perimeter = sum(len(r) * perimeter(r) for r in regions)

    return total_perimeter


if __name__ == "__main__":
    filename = 'example.txt'
    print(f'permimeter for example file is  : {calculate_perimeter(filename)}')
    filename = 'day12_input.txt'
    print(f'permimeter for input file is  : {calculate_perimeter(filename)}')