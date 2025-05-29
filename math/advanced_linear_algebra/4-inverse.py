#!/usr/bin/env python3
"""This module contains functions to calculate the inverse of a matrix."""


def determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    Args:
        matrix (list of lists): A non-empty square matrix.

    Returns:
        float or int: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square or is empty.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        if matrix == [[]]:
            return 1
        raise ValueError("matrix must be a square matrix")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a square matrix.

    Args:
        matrix (list of lists): A non-empty square matrix.

    Returns:
        list of lists: The cofactor matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square or is empty.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    cof_matrix = []
    for i in range(n):
        row_cofactors = []
        for j in range(n):
            sub_matrix = [row[:j] + row[j + 1:]
                          for k, row in enumerate(matrix) if k != i]
            minor = determinant(sub_matrix)
            sign = (-1) ** (i + j)
            row_cofactors.append(sign * minor)
        cof_matrix.append(row_cofactors)

    return cof_matrix


def adjugate(matrix):
    """
    Calculates the adjugate (adjoint) of a square matrix.

    Args:
        matrix (list of lists): A non-empty square matrix.

    Returns:
        list of lists: The adjugate matrix.
    """
    return [list(row) for row in zip(*cofactor(matrix))]


def inverse(matrix):
    """
    Calculates the inverse of a square matrix.

    Args:
        matrix (list of lists): A non-empty square matrix.

    Returns:
        list of lists: The inverse matrix, or None if the matrix is singular.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)
    return [[element / det for element in row] for row in adj]
