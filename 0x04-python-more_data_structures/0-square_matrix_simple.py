#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    tmp = []
    i = 0
    for row in matrix:
        tmp = list(map(lambda x: x*x, row))
        new_matrix.append(tmp)
    new_matrix.pop(0)
    return new_matrix
