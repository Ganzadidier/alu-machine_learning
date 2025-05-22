#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    # Check axis validity
    if axis == 0:
        # Ensure same number of columns
        if len(mat1) == 0 or len(mat2) == 0 or len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        # Ensure same number of rows
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        return None
