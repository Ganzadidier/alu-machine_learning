#!/usr/bin/env python3
"""
Provides a function to transpose a matrix-like object.
"""


def np_transpose(matrix):
    """
    Returns the transpose of a matrix-like object.

    The function assumes the input supports the `.transpose()` method,
    such as a NumPy ndarray.

    Args:
        matrix: A matrix-like object with a transpose method.

    Returns:
        The transposed matrix.

    Example:
        >>> import numpy as np
        >>> mat = np.array([[1, 2], [3, 4]])
        >>> np_transpose(mat)
        array([[1, 3],
               [2, 4]])
    """
    return matrix.transpose()
