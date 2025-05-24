#!/usr/bin/env python3
"""
cat_arrays module

This module provides a function to concatenate two arrays (lists).
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays.

    Parameters:
        arr1 (list): The first list.
        arr2 (list): The second list.

    Returns:
        list: A new list containing the elements of arr1 followed by
              the elements of arr2.

    Example:
        cat_arrays([1, 2, 3], [4, 5]) -> [1, 2, 3, 4, 5]
    """
    return arr1 + arr2
