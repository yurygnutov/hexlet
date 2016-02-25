__author__ = 'yury'

# Identify the color of a square of the chessboard. Square A1 is black.

# Example:
# "black" == solution("A", 1)

def solution_old(a, n):
    if a in "ACEG":
        return "black" if n % 2 else "white"
    else:
        return "black" if not n % 2 else "white"


def solution(a, b):
    return "black" if ord(a) % 2 == b % 2 else "white"