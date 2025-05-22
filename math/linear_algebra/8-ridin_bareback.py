#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    # Validate multiplication dimensions: cols of mat1 == rows of mat2
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
