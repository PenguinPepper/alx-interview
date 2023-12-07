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
            rounds +=1
    if (len(available_nums) <= 1):
        winners.append(i)
    if len(set(winners)) == 1:
        if (winners[0] % 2 == 0):
            return "Ben"
        else:
            return "Maria"
    else:
        return None
