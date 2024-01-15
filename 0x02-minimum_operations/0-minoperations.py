#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations needed for each position
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    # Iterate through each position
    for i in range(2, n + 1):
        # If i is prime, find the smallest factor and update dp[i]
        if n % i == 0:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
                    break

            # Update dp[i] with the other factor
            dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n]

# Testing the provided examples
n1 = 4
print("Min number of operations to reach {} characters: {}".format(n1, minOperations(n1)))

n2 = 12
print("Min number of operations to reach {} characters: {}".format(n2, minOperations(n2)))
