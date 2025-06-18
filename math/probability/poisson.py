#!/usr/bin/env python3
"""
Module: poisson
Defines a class Poisson that represents a Poisson distribution.
"""

from math import exp, factorial


class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): The expected number of occurrences in a given time.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes a Poisson distribution instance.

        Args:
            data (list, optional): List of data to estimate the distribution.
            lambtha (float, optional): Expected number of occurrences.

        Raises:
            TypeError: If data is provided and is not a list.
            ValueError: If lambtha is negative or data has fewer than two.
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
        Calculates the value of the PMF (Probability Mass Function)
        for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: The PMF value for k.
        """
        try:
            k = int(k)
        except Exception:
            return 0

        if k < 0:
            return 0

        lamb = self.lambtha
        return (lamb ** k) * exp(-lamb) / factorial(k)


    def cdf(self, k):
        """
        Calculates the CDF (Cumulative Distribution Function)
        for a given number of successes.

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
            cdf_value += (lamb ** i) * exp(-lamb) / factorial(i)
        return cdf_value
