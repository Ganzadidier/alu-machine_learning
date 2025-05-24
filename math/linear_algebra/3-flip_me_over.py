#!/usr/bin/env python3
"""
matrix_transpose module

This module provides a function to compute the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Computes the transpose of a 2D matrix.

    The transpose of a matrix is obtained by flipping it over its diagonal,
    switching the row and column indices of the matrix.

    Parameters:
        matrix (list of lists): A 2D matrix represented as a list of lists,
                                where each sub-list is a row of the matrix.

    Returns:
        list of lists: The transposed matrix.

    Example:
        matrix_transpose([[1, 2], [3, 4], [5, 6]])
        -> [[1, 3, 5], [2, 4, 6]]
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
