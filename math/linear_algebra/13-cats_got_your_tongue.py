#!/usr/bin/env python3
"""Concatenates two matrices along a specified axis."""

import numpy as np

def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (np.ndarray): The first matrix.
        mat2 (np.ndarray): The second matrix.
        axis (int): The axis along which to concatenate.

    Returns:
        np.ndarray: The concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
