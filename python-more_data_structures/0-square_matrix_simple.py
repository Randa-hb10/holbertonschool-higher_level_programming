#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    value = []

    for lst in matrix:
        matrix_lst = []
        for num in lst:
            matrix_lst.append(num ** 2)
        value.append(matrix_lst)

    return value
