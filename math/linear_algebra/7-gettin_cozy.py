#!/usr/bin/env python3
"""
Concatenates two 2D matrices along a specified axis without using external libraries.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along the specified axis.

    This function joins two matrices (lists of lists) either by rows (axis=0)
    or by columns (axis=1), provided their dimensions are compatible.

    Args:
        mat1 (list of list of int/float): The first 2D matrix.
        mat2 (list of list of int/float): The second 2D matrix.
        axis (int): Axis to concatenate along.
                    - 0 to concatenate by rows (vertically)
                    - 1 to concatenate by columns (horizontally)

    Returns:
        list of list: The concatenated 2D matrix,
                      or None if dimensions are incompatible.

    Examples:
        >>> cat_matrices2D([[1, 2]], [[3, 4]], axis=0)
        [[1, 2], [3, 4]]

        >>> cat_matrices2D([[1], [2]], [[3], [4]], axis=1)
        [[1, 3], [2, 4]]
    """
    if axis == 0:
        # Ensure both matrices have the same number of columns
        if len(mat1) == 0 or len(mat2) == 0 or len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    if axis == 1:
        # Ensure both matrices have the same number of rows
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    return None
