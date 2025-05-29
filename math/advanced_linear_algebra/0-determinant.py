#!/usr/bin/env python3
"""
This module contains a function to calculate the determinant of a matrix.
"""


def determinant(matrix):
    """Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): A square matrix.

    Returns:
        int or float: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """
    # Validate input is a list of lists
    if (not isinstance(matrix, list) or
	 not all(isinstance(row, list) for row in matrix)):
		raise TypeError("matrix must be a list of lists")


    # Validate matrix is square
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        if matrix == [[]]:
            return 1  # 0x0 matrix
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive case for nxn matrix
    det = 0
    for col in range(n):
        # Get minor matrix
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        # Recursive call and cofactor expansion
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det
