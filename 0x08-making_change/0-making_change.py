#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    # Iterate through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make that total
    return dp[total] if dp[total] != float('inf') else -1
