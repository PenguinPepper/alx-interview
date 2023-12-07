#!/usr/bin/python3
"""Module contains the function isWinner"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    """
    rounds = 0
    winners = []
    while rounds <= x:
        available_nums = nums[:]
        for i in range(len(available_nums)):
            left_nums = []
            for num in available_nums:
                if num % available_nums[i] != 0:
                    left_nums.append(num)
            available_nums = left_nums
            if (len(available_nums) <= 1):
                winners.append(i)
                break
        rounds += 1
    freq = {i: winners.count(i) for i in winners}
    max_freq = max(freq.values())
    winners = [player for player, count in freq.items() if count == max_freq]
    if len(winners) == 1:
        if winners[0] == 0:
            return "Maria"
        else:
            return "Ben"
    else:
        return None
