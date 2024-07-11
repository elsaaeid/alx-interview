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

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        if n % i == 0:
            operations[i] = i
            continue
        for j in range(i // 2, 1, -1):
            if i % j == 0:
                operations[i] = operations[j] + (i // j)
                break

    return operations[n]
