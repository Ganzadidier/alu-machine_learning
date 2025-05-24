#!/usr/bin/env python3
"""
Performs matrix multiplication using NumPy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication between two NumPy ndarrays.

    Args:
        mat1 (np.ndarray): First input matrix.
        mat2 (np.ndarray): Second input matrix.

    Returns:
        np.ndarray: Result of the matrix multiplication.

    Example:
        np_matmul(np.array([[1, 2]]), np.array([[3], [4]]))
        -> array([[11]])
    """
    return np.matmul(mat1, mat2)
