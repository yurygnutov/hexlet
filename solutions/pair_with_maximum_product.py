__author__ = 'yury'


# Given an array with both positive and negative integers,
# return a pair of integers that, when multiplied,
# would produce the largest possible number.
# An element can only be used once, in other words, you cannot multiply a number by itself.
# Elements of the pair should be arranged in ascending order.

# Example:
# [-4,-3] == solution([-1,-2,-4,-3,0,3,2,1])

from itertools import permutations
from functools import reduce
import operator

def solution_old(seq):
    pairs = list(permutations(seq, 2))
    return sorted(list(sorted(pairs, key=lambda x: x[0] * x[1])[-1]))


def solution(seq):
    return max(permutations(seq, 2), key=lambda x: reduce(operator.mul, x))
