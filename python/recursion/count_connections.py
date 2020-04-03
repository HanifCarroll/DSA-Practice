from typing import List


def count_connections(grid: List[List], row: int, col: int) -> int:
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return 0
    
    if grid[row][col] == 0:
        return 0
    
    grid[row][col] = 0
    connections = 1
    connections += count_connections(grid, row-1, col-1)
    connections += count_connections(grid, row-1, col)
    connections += count_connections(grid, row, col-1)
    connections += count_connections(grid, row+1, col)
    connections += count_connections(grid, row, col+1)
    connections += count_connections(grid, row+1, col+1)
    # for r in range(row-1, row+2):
    #     for c in range(col-1, col+2):
    #         if r != row and c != col:
    #             connections += count_connections(grid, r, c)
    return connections

def find_largest_area(grid: List[List]) -> int:
    largest_area = 0

    for row_index, row in enumerate(grid):
        for col_index, _ in enumerate(row):
            area = count_connections(grid, row_index, col_index)
            largest_area = max(largest_area, area)

    return largest_area

grid = [
    [0,1,1,0,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [1,1,0,0,1],
]
print(find_largest_area(grid))