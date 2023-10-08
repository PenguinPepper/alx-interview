#!/usr/bin/python3
"""Psscals triangle"""


def pascal_triangle(n):
    """"Pascals triangle"""
    if (n <= 0):
        return []
    new_list = [[1]]
    for i in range(1, n):
        sec_list = [1]
        for j in range(1, i):
            num = new_list[i - 1][j - 1] + new_list[i - 1][j]
            sec_list.append(num)
        sec_list.append(1)
        new_list.append(sec_list)
    return new_list
