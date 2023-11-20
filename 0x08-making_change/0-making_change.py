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
    if max(coins) < total:
        remainder = total - max(coins)
    else:
        remainder = total
    multiples = []
    for i in coins:
        if remainder % i == 0:
            multiples.append(i)
    if not multiples:
        return -1
    other_coins = 0
    for j in multiples:
        if (remainder / j).is_integer():
            other_coins += remainder / j
    if other_coins % 2 == 0:
        other_coins = other_coins / 2
    return int(other_coins)
