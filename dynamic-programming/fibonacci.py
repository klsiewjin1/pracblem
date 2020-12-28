"""
Followed along to https://www.youtube.com/watch?v=oBt53YbR9Kk&t=12114s&ab_channel=freeCodeCamp.org
"""
from math import sqrt


def fib_memoization(n, hash_table=None):
    """
    Memoization of the traditional recursive function to get the n-th element in the Fibonacci sequence
    """
    if hash_table is None:
        hash_table = dict()
    if n in hash_table:
        return hash_table[n]
    if n <= 2:
        return 1

    hash_table[n] = fib_memoization(n - 1, hash_table) + fib_memoization(n - 2, hash_table)
    return hash_table[n]


def fib_tabulation(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for x in range(2, len(arr)):
        arr[x] = arr[x - 2] + arr[x - 1]
    return arr[n]


def fib_Binet(n):
    """For given n, determine if is part of the Fibonacci sequence"""
    tmp = pow(n, 2) * 5
    if sqrt(tmp - 4).is_integer():
        return True
    elif sqrt(tmp + 4).is_integer():
        return True
    return False


if __name__ == "__main__":
    print(fib_memoization(6), fib_tabulation(6))
    print(fib_memoization(7), fib_tabulation(7))
    print(fib_memoization(8), fib_tabulation(7))
    print(fib_memoization(50), fib_tabulation(50))
