#!/usr/bin/env python3
"""
Performs element-wise operations on two matrices or arrays.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1: A matrix-like object (e.g., NumPy ndarray) that supports
              element-wise operations.
        mat2: Another matrix-like object or scalar compatible with mat1.

    Returns:
        tuple: A tuple containing four results:
            - Element-wise addition (mat1 + mat2)
            - Element-wise subtraction (mat1 - mat2)
            - Element-wise multiplication (mat1 * mat2)
            - Element-wise division (mat1 / mat2)

    Example:
        >>> np_elementwise([[1, 2]], [[3, 4]])
        ([[4, 6]], [[-2, -2]], [[3, 8]], [[0.333..., 0.5]])
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
