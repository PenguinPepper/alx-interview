#!/usr/bin/python3
"""module contains minOperations function"""


def minOperations(n):
    """Find the minimum number of operations needed
    to get to n number of 'H' characters in a file

    n: number of characters in the file
    """
    if (n <= 1):
        return 0
    for i in range(2, n + 1):
        if (n % i == 0):
            return i + minOperations(n // i)
    return n
