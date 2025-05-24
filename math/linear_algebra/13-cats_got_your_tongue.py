#!/usr/bin/env python3
"""
Concatenates two matrices along a specified axis using NumPy.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two NumPy matrices (arrays) along a specified axis.

    This function wraps NumPy's concatenate method to join two arrays
    along the given axis. Both arrays must have the same shape, except
    in the dimension corresponding to the specified axis.

    Args:
        mat1 (np.ndarray): The first matrix to concatenate.
        mat2 (np.ndarray): The second matrix to concatenate.
        axis (int): The axis along which the matrices will be concatenated.
                    Must be a valid axis for the given arrays.

    Returns:
        np.ndarray: The concatenated matrix.

    Raises:
        ValueError: If the arrays cannot be concatenated along the given axis.

    Example:
        np_cat(np.array([[1, 2]]), np.array([[3, 4]]), axis=0)
        -> array([[1, 2],
                  [3, 4]])

        np_cat(np.array([[1], [2]]), np.array([[3], [4]]), axis=1)
        -> array([[1, 3],
                  [2, 4]])
    """
    return np.concatenate((mat1, mat2), axis=axis)
