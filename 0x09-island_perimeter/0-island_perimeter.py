#!/usr/bin/python3
"""Module contsins island_perimeter"""

def island_perimeter(grid):
    """grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that
    isn’t connected to the water surrounding the island)."""
    ones = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                ones += 4
                if (i > 0 and grid[i - 1][j] == 1):
                    ones -= 2
                if (j > 0 and grid[i][j - 1] == 1):
                    ones -= 2
    return ones
