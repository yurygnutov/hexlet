__author__ = 'yury'

# Given an array, possibly with more arrays inside,
# return a 1-dimensional flat array with all the values in the initial order.

# Example:
# [1,2,{"a":"b"}] == solution([1,[2,[{"a":"b"}]]])


def solution(seq, result=None):
    if result == None:
        result = []
    for v in seq:
        if isinstance(v, list):
            solution(v, result)
        else:
            result.append(v)
    return result
