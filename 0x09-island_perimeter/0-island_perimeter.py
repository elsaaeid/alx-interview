#!/usr/bin/python3
"""
To calculate the perimeter of an island represented in a grid
"""


def island_perimeter(grid):
    """
    function will iterate through the grid and for each land cell
    (represented by 1), it will check its four neighboring cells
    (up, down, left, right) to determine how many sides of the
    land cell are exposed to water (represented by 0) or
    the edge of the grid.
    """
    peri = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Check if the cell is land
                peri += 4  # Start by assuming all four sides are exposed
                # Check the four directions
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    peri -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check below
                    peri -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    peri -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                    peri -= 1

    return peri
