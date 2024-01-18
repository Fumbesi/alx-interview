#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    # Initialize an array to store the minimum number of operations for each index
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # If i is a factor of n, it means we can copy from i and paste (n//i) times
        for j in range(2 * i, n + 1, i):
            dp[j] = min(dp[j], dp[i] + j // i)

    return dp[n] if dp[n] != float('inf') else 0

# Test cases
if __name__ == "__main__":
    n1 = 4
    print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))
