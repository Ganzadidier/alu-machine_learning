#!/usr/bin/env python3
"""Performs element-wise operations on two matrices or a matrix and a scalar."""

import numpy as np

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division
    on two matrices or a matrix and a scalar.

    Args:
        mat1 (np.ndarray): First input matrix or scalar-compatible array.
        mat2 (np.ndarray or scalar): Second input matrix or scalar.

    Returns:
        tuple: Contains 4 np.ndarrays:
            - element-wise sum
            - element-wise difference
            - element-wise product
            - element-wise quotient
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
