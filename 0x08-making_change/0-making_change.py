#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total <= 0:
            break
    return count if total == 0 else -1
    # if total <= 0:
    #     return 0
    # dp = [float('inf')] * (total + 1)
    # dp[0] = 0

    # for amount in range(1, total + 1):
    #     for coin in coins:
    #         if coin <= amount:
    #             dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # return -1 if dp[total] == float('inf') else dp[total]
