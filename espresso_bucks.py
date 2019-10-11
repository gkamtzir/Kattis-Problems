def check_coverage(grid, width, height, i, j):
    if i - 1 >= 0:
        if grid[i - 1][j] == "E":
            return True
    if j - 1 >= 0:
        if grid[i][j - 1] == "E":
            return True
    return False

height, width = map(int, input().split())

# Initializing the grid.
grid = []

# Input.
for i in range(height):
    grid.append(list(input()))

# Main Loop.
for i in range(height):
    prev = []
    for j in range(width):
        if grid[i][j] == "#":
            # Checking if there is a 'land' waiting
            # for a coffee shop.
            if len(prev) != 0:
                grid[prev[0]][prev[1]] = "E"
                prev = []
            continue
        # Checking if the current 'land' is served
        # by a coffee shop.
        if check_coverage(grid, width, height, i, j):
            if len(prev) != 0:
                grid[prev[0]][prev[1]] = "E"
                prev = []
            continue
        else:
            # Checking if the previous point was a 'land'
            # that's waiting for a coffee shop.
            if len(prev) == 0:
                prev = [i, j]
                continue
            else:
                grid[i][j] = "E"
                prev = []
    if len(prev) != 0:
        grid[prev[0]][prev[1]] = "E"

# Printing out the results.
for row in grid:
    print("".join(row))
