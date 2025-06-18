#!/usr/bin/env python3
"""
Module: poisson
Defines a class Poisson that represents a Poisson distribution.
"""

class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): The expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes a Poisson distribution instance.

        Args:
            data (list, optional): List of data to estimate the distribution.
            lambtha (float, optional): Expected number of occurrences.

        Raises:
            TypeError: If data is provided and is not a list.
            ValueError: If lambtha is not positive or data has fewer than two values.
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
