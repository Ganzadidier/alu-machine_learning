#!/usr/bin/env python3
"""
matrix_shape module

This module provides a function to determine the shape of a matrix
represented as nested lists.
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    The matrix can be nested to represent higher-dimensional arrays
    (e.g., 2D, 3D, etc.). The shape is returned as a list where each
    element represents the size of the matrix along that dimension.

    Parameters:
        matrix (list): A list of lists (or nested lists) representing
                       the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.

    Example:
        matrix_shape([[1, 2], [3, 4]]) -> [2, 2]
        matrix_shape([[[1], [2]], [[3], [4]]]) -> [2, 2, 1]
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
