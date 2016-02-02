__author__ = 'yury'

# Given an array that represents elements of an arithmetic progression in order.
# One element is missing in the progression.
# Return the missing number.
# Example:
# 6 == solution([2,4,8,10,12,14])

def solution(p):
    new = []
    step = p[0] - p[1] if p[0] - p[1] == p[1] - p[2] else p[-1] - p[-2]
    for k in range(p[0], p[-1], step):
        new.append(k)
    return set(new).difference(set(p)).pop()
