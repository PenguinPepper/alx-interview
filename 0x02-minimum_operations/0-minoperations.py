#!/usr/bin/python3
"""module contains minOperations function"""


def minOperations(n):
    """Returns an int"""
    if( n <= 7):
        return n
    elif(n % 3 == 0):
        return n // 3 + 3
    elif(n % 2 == 0):
        return n // 2 + 1
    else:
        return 0
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""
