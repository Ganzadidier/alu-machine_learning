#!/usr/bin/env python3
"""
np_shape module

This module provides a function that returns the shape of a NumPy array.
"""

import numpy as np


def np_shape(matrix):
    """
    Returns the shape of a NumPy array.

    Parameters:
        matrix (numpy.ndarray): A NumPy array.

    Returns:
        tuple: A tuple representing the dimensions of the array.

    Example:
        np_shape(np.array([[1, 2], [3, 4]])) -> (2, 2)
    """
    return matrix.shape
