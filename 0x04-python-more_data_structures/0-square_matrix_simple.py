#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # List comprehension to create a new matrix with elements squared
    return [[column**2 for column in row] for row in matrix]

