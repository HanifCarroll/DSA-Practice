def print_grid(grid):
    for row in grid:
        print(row)

values = {
    'water': 10,
    'book': 3,
    'food': 9,
    'jacket': 5,
    'camera': 6
}

weights = {
    'water': 3,
    'book': 1,
    'food': 2,
    'jacket': 2,
    'camera': 1
}

values = [10, 3, 9, 5, 6]
weights = [3, 1, 2, 2, 1]

def solve(weights, values, capacity):
    grid = [[0] * (capacity + 1) for i in range(len(values))]
    # print_grid(grid)
    
    for row_index, row in enumerate(grid):
        item_cost = weights[row_index]
        for capacity, col in enumerate(row):
            remaining_capacity = capacity - item_cost
            if remaining_capacity < 0:
                if row_index == 0:
                    continue
                else:
                    grid[row_index][capacity] = grid[row_index-1][capacity]
            else:
                value_of_item = values[row_index]
                if row_index == 0:
                    grid[row_index][capacity] = value_of_item
                if row_index > 0:
                    value_with_item = value_of_item + grid[row_index - 1][remaining_capacity]
                    grid[row_index][capacity] = max(grid[row_index-1][capacity]
                                                    , value_with_item)
    
    print_grid(grid)

solve(weights, values, 6)
