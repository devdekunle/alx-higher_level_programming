#!/usr/bin/python3
"""
This module contains a function that divides each element of a matrix by a number
and returns a new matrix with the values of the divided elements.
The function also considers different cases and also edge cases which could
limit the effectiveness of the program.
"""
def matrix_divided(matrix, div):
    """ This function divides each element of the matix by div
    Arg: 
    matrix: a list of lists
    div: number to divide each element of the matrix
    Return: new_matrix"""

    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif div is None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'div'")
    else:
        new_matrix = []
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError("Each row of the matrix must have the same size")
            new_row = []
            for elem in row:
                
                if type(elem) not in [float, int]:
                    raise TypeError("element must be a float or an integer")
                else:
                    elem = round((elem / div), 2)
                    new_row.append(elem)
            new_matrix.append(new_row)
        return new_matrix
