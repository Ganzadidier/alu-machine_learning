#!/usr/bin/env python3
"""
cat_matrices2D module

This module provides a function to concatenate two 2D matrices along
a specified axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along the specified axis.

    Parameters:
        mat1 (list of lists): The first 2D matrix.
        mat2 (list of lists): The second 2D matrix.
        axis (int): The axis along which to concatenate (0 for rows, 1 for columns).

    Returns:
        list of lists or None: The concatenated 2D matrix, or None if the matrices
                               cannot be concatenated along the specified axis.

    Examples:
        cat_matrices2D([[1, 2]], [[3, 4]]) -> [[1, 2], [3, 4]]
        cat_matrices2D([[1], [2]], [[3], [4]], axis=1) -> [[1, 3], [2, 4]]
    """
    if axis == 0:
        # Ensure both matrices have the same number of columns
        if len(mat1) == 0 or len(mat2) == 0 or len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        # Ensure both matrices have the same number of rows
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        return None
