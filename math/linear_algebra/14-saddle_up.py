#!/usr/bin/env python3
"""Performs matrix multiplication using NumPy."""

import numpy as np

def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication between two numpy ndarrays.

    Args:
        mat1 (np.ndarray): First input matrix.
        mat2 (np.ndarray): Second input matrix.

    Returns:
        np.ndarray: Result of the matrix multiplication.
    """
    return np.matmul(mat1, mat2)
