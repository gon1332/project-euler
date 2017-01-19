#!/usr/bin/env python
# -*- coding: utf-8 -*-

def load_grid(file_name):
    with open(file_name, 'r') as f:
        grid_raw = f.read()

    grid_lines = grid_raw.split('\n')
    grid_lines.pop()    # Pop the last redundant empty line

    return [list(map(int, line.split(' '))) for line in grid_lines]


def print_grid(grid):
    for i in range(len(grid)):
        for j in grid[i]:
            print('{0:2d}'.format(j), end=' ')
        print()

if __name__ == '__main__':
    grid = load_grid('grid.txt')

    max_prod = 0
    row_size = len(grid)
    col_size = len(grid[0]) 
    for i in range(row_size):
        for j in range(col_size):
            # horizontal
            if j <= col_size-4:
                h_prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3];
                max_prod = max(max_prod, h_prod)
                
            # vertical
            if i <= row_size-4:
                v_prod = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j];
                max_prod = max(max_prod, v_prod)

            # diagonal (down-right)
            if i <= row_size-4 and j <= col_size-4:
                d_prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3];
                max_prod = max(max_prod, d_prod)

            # diagonal (up-right)
            if i >= 4 and j <= col_size-4:
                d_prod = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3];
                max_prod = max(max_prod, d_prod)

    print(max_prod)
