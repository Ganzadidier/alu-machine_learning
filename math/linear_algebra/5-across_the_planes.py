#!/usr/bin/env python3
"""
Module to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of list of int/float): First 2D matrix.
        mat2 (list of list of int/float): Second 2D matrix.

    Returns:
        list of list of int/float: A new 2D matrix representing the element-wise sum.
        None: If the input matrices are not the same shape.
    """
    if not mat1 or not mat2:
        return None

    if len(mat1) != len(mat2):
        return None

    result = []

    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
        result.append([a + b for a, b in zip(row1, row2)])

    return result
