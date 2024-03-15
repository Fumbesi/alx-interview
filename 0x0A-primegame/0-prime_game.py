#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(n):
    """Generate all prime numbers up to n."""
    primes = []
    sieve = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
    return primes


def isWinner(x, nums):
    """Determine the winner of each game."""
    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    # Play each round
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    # Determine the winner with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
