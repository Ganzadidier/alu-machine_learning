#!/usr/bin/env python3
"""
np_transpose module

This module provides a function that returns the transpose of a NumPy array.
"""

import numpy as np


def np_transpose(matrix):
    """
    Returns the transpose of a NumPy array.

    Parameters:
        matrix (numpy.ndarray): A NumPy array.

    Returns:
        numpy.ndarray: The transposed array.

    Example:
        np_transpose(np.array([[1, 2], [3, 4]]))
        -> array([[1, 3],
                  [2, 4]])
    """
    return matrix.transpose()
