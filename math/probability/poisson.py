#!/usr/bin/env python3
"""
Module: poisson
Defines a class Poisson that represents a Poisson distribution.
"""


class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): Expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes a Poisson distribution instance.

        Args:
            data (list, optional): List of data to estimate the distribution.
            lambtha (float, optional): Expected number of occurrences.

        Raises:
            TypeError: If data is not a list.
            ValueError: If lambtha is not positive or data has fewer than two.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: PMF value for k, or 0 if k is invalid.
        """
        try:
            k = int(k)
        except Exception:
            return 0

        if k < 0:
            return 0

        lamb = self.lambtha
        return (lamb ** k) * self._exp(-lamb) / self._factorial(k)

    def cdf(self, k):
        """
        Calculates the CDF for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: CDF value for k, or 0 if k is invalid.
        """
        try:
            k = int(k)
        except Exception:
            return 0

        if k < 0:
            return 0

        lamb = self.lambtha
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += (lamb ** i) * self._exp(-lamb) / self._factorial(i)
        return cdf_value

    def _factorial(self, n):
        """
        Computes the factorial of a number manually.

        Args:
            n (int): Non-negative integer.

        Returns:
            int: Factorial of n.
        """
        result = 1
         for i in range(2, n + 1):
            result *= i
        return result


    def _exp(self, x):
        """
        Approximates the exponential of x using a Taylor series.

        Args:
            x (float): The exponent.

        Returns:
            float: Approximation of e^x.
        """
        result = 1.0
        term = 1.0
        for i in range(1, 100):
            term *= x / i
            if abs(term) < 1e-10:  # precision threshold
                break
            result += term
        return result
