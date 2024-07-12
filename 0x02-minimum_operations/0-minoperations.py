#!/usr/bin/python3
"""
minimum_operations
"""


def minOperations(n):
    """
    A method that calculates the fewest number of
    operations needed to result in exactly n H characters
    """
    i = 0
    j = 2
    while n > 1:
        while n % j == 0:
            i += j
            n /= j
        j += 1
    return i
