#!/usr/bin/python3
"""
The minimum operations.
"""

def minOperations(n):
    """A method that computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if n <= 1:
                return 0

                operations = 0
                    divisor = 2

                        while n > 1:
                                    while n % divisor == 0:
                                                    operations += divisor
                                                                n //= divisor
                                                                        divisor += 1

                                                                            return operations
