#!/usr/bin/env python3
"""
mat_mul module

This module provides a function to perform matrix multiplication
on two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two 2D matrices (mat1 and mat2).

    Matrix multiplication is only possible if the number of columns in mat1
    equals the number of rows in mat2. The result is a new matrix where
    each element is the dot product of a row from mat1 and a column from mat2.

    Parameters:
        mat1 (list of lists): The first 2D matrix.
        mat2 (list of lists): The second 2D matrix.

    Returns:
        list of lists or None: The resulting 2D matrix after multiplication,
                               or None if the matrices cannot be multiplied.

    Example:
        mat_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[19, 22], [43, 50]]
    """
    # Validate multiplication dimensions: columns of mat1 == rows of mat2
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for row in mat1:
        new_row = []
        for j in range(len(mat2[0])):
            sum_product = 0
            for k in range(len(mat2)):
                sum_product += row[k] * mat2[k][j]
            new_row.append(sum_product)
        result.append(new_row)

    return result
