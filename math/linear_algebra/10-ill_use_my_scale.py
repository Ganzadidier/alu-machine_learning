#!/usr/bin/env python3
"""
Provides a function to retrieve the shape of a matrix-like object.
"""


def np_shape(matrix):
    """
    Returns the shape of a matrix-like object.

    The function assumes that the input has a `.shape` attribute,
    such as a NumPy ndarray.

    Args:
        matrix: A matrix-like object with a shape attribute.

    Returns:
        tuple: A tuple representing the shape of the matrix.

    Example:
        >>> import numpy as np
        >>> mat = np.array([[1, 2], [3, 4]])
        >>> np_shape(mat)
        (2, 2)
    """
    return matrix.shape
