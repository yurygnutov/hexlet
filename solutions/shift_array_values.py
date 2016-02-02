__author__ = 'yury'

# Given an array and a number,
# generate an array with values shifted left or right by a given number.
# The number could be positive or negative;
# positive number shifts the array forward, negative shifts it backwards.
# Example:
# [4,5,1,2,3] == solution(-2, [1,2,3,4,5])

def solution(b, a):
    b %= len(a)
    return a[b:] + a[:b]
