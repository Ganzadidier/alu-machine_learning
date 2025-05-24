#!/usr/bin/env python3
"""
Performs element-wise addition of two 2D matrices.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    This function checks that both matrices have the same dimensions
    and returns a new matrix containing the element-wise sum.
    If the matrices are not the same shape, it returns None.

    Args:
        mat1 (list of list of int/float): The first 2D matrix.
        mat2 (list of list of int/float): The second 2D matrix.

    Returns:
        list of list of int/float or None: The element-wise sum of the two
        matrices, or None if they have incompatible dimensions.

    Example:
        >>> add_matrices2D([[1, 2]], [[3, 4]])
        [[4, 6]]
    """
    if len(mat1) != len(mat2) or 
	any(len(r1) != len(r2) for r1, r2 in zip(mat1, mat2)):
        return None

    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
