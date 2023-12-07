#!/usr/bin/python3
"""module contains nqueens script that solves the N queens problem.
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1 The
program should print every possible solution to the problem
One solution per line

no two queens threaten each other; thus, a solution requires
that no two queens share the same row, column, or diagonal.
"""
import sys


if (len(sys.argv) <= 1):
    print("Usage: nqueens N")
    sys.exit(1)
else:
    try:
        num = int(sys.argv[1])
    except ValueError as error:
        print("N must be a number")
        sys.exit(1)
    else:
        if (num < 4):
            print("N must be at least 4")
            sys.exit(1)
        else:
            for i in range(num):
                formatted_solutin = [[i, num - 1]]
                print(formatted_solution)
