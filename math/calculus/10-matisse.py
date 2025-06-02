#!/usr/bin/env python3
"""
poly_derivative.py

This module contains a function to compute the derivative of a polynomial
represented as a list of coefficients.
"""

def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): A list of coefficients where the index represents the
                     power of x (e.g., [5, 3, 0, 1] represents x^3 + 3x + 5).

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
              Returns [0] if the derivative is zero.
              Returns None if the input is invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(c, (int, float)) for c in poly):
        return None

    # Compute the derivative: d/dx of a_n * x^n = n * a_n
    derivative = [i * poly[i] for i in range(1, len(poly))]

    # Return [0] if the derivative is all zeros
    return derivative if any(derivative) else [0]
