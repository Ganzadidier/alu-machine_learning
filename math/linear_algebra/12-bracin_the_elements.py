#!/usr/bin/env python3
"""Performs element-wise operations on two matrices."""

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1: A NumPy ndarray.
        mat2: A NumPy ndarray or scalar.

    Returns:
        tuple: (add, subtract, multiply, divide) results, each as a NumPy ndarray.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
