#!/usr/bin/env python3
"""
This module contains a function to determine the definiteness of a matrix.
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of a matrix.

    Args:
        matrix (numpy.ndarray): The matrix definiteness is to be calculated.

    Returns:
        str or None: One of the following strings:
            - 'Positive definite'
            - 'Positive semi-definite'
            - 'Negative definite'
            - 'Negative semi-definite'
            - 'Indefinite'
            Or None if the matrix is not valid for definiteness analysis.

    Raises:
        TypeError: If matrix is not a numpy.ndarray
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if matrix.size == 0:
        return None

    # Check if the matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    elif np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"
    else:
        return None
