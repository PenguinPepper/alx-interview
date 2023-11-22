#!/usr/bin/python3
"""Module contains makeChnage function"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount total
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each
    denomination of coin in the list
    """
    change = [float('inf')] * (total + 1)
    change[0] = 0
    for i in coins:
        for j in range(i, total + 1):
            change[j] = min(change[j], change[j - i] + 1)
    if change[total] != float('inf'):
        return int(change[total])
    else:
        return -1
