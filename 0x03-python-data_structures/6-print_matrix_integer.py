#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    row_size = len(matrix)
    column_size = 0
    i = 0
    while i < row_size:
        column_size = len(matrix[i])
        j = 0
        while j < column_size:
            print("{:d}".format(matrix[i][j]), end='')
            if j == column_size - 1:
                print("\n", end='')
            else:
                print(" ", end='')
            j += 1
        i += 1
