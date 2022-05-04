#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        row = map(lambda n: n * n, matrix[i])
        square_matrix.append(list(row))
    return square_matrix
