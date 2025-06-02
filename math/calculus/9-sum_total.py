#!/usr/bin/env python3
"""
summation_i_squared.py

This module contains a recursive function to calculate the summation of
squares from 1 to n, i.e., ∑(i^2) for i = 1 to n.
"""

def summation_i_squared(n):
    """
    Calculates the sum of squares from 1 to n using recursion.

    Args:
        n (int): The upper bound of the summation (inclusive).

    Returns:
        int: The sum of squares from 1 to n.
             Returns None if the input is not a valid positive integer.
    """
    if not isinstance(n, int) or n < 1:
        return None

    if n == 1:
        return 1

    return n * n + summation_i_squared(n - 1)
