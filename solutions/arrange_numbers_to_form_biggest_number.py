__author__ = 'yury'

# Construct the largest possible number by arranging the integers from the given array.
# Since the resulting number can be very large and out of int range, you have to represent it as string.
# For example, from [3, 24, 4] we can construct 6 different numbers:
# 3244, 3424, 2434, 2443, 4324, 4243 and the largest of them is 4324.

# Example:
# "998764543431" == solution([1,34,3,98,9,76,45,4])


from itertools import product

def solution_wrong(seq):
    p = [k for k in list(product(seq, repeat=len(seq))) if len(set(k)) == len(k)]
    return str(max([int("".join(map(str, k))) for k in p]))


#  won't work for examples like this:
#  >>> solution([22, 22])


def solution(x):
    x = list(map(str, x))
    return "".join(sorted(x, reverse=True, key=lambda s: s.ljust(max(map(len, x)), "0")))
