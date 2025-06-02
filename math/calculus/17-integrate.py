#!/usr/bin/env python3
"""
poly_integral.py

This module contains a function to compute the indefinite integral
of a polynomial represented as a list of coefficients.
"""

def poly_integral(poly, C=0):
    """
    Calculates the indefinite integral of a polynomial.

    Args:
        poly (list): A list of coefficients where the index represents the
                     power of x (e.g., [5, 3, 0, 1] represents x^3 + 3x + 5).
        C (int or float): The constant of integration. Default is 0.

    Returns:
        list: A list of coefficients representing the integral of the polynomial,
              starting with the constant of integration. Coefficients that are
              whole numbers are returned as integers.
              Returns None if the input is invalid.
    """
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None

    if not isinstance(C, (int, float)):
        return None

    # Start with the constant of integration
    result = [C]

    # Compute the integral for each term
    for i, coeff in enumerate(poly):
        integral_coeff = coeff / (i + 1)

        # Convert to int if coefficient is a whole number
        if integral_coeff.is_integer():
            integral_coeff = int(integral_coeff)

        result.append(integral_coeff)

    # Remove unnecessary trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result
