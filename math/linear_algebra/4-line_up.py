#!/usr/bin/env python3
"""
add_arrays module

This module provides a function to perform element-wise addition
of two arrays (lists of numbers).
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    If the arrays are not of the same length, the function returns None.

    Parameters:
        arr1 (list): The first list of numbers.
        arr2 (list): The second list of numbers.

    Returns:
        list or None: A list containing the element-wise sum of arr1 and arr2,
                      or None if the input lists have different lengths.

    Example:
        add_arrays([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
        add_arrays([1, 2], [1]) -> None
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
