#!/usr/bin/python3
"""
this module defines the function isWinner
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes. """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p]):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count how many primes are <= n
        prime_count = sum(1 for p in primes if p <= n)

        # Determine the winner based on the count of primes
        if prime_count % 2 == 1:
            maria_wins += 1  # Maria wins if the count of primes is odd
        else:
            ben_wins += 1    # Ben wins if the count of primes is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
