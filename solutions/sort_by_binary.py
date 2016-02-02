__author__ = 'yury'

# Sort an array of integers by the number of 1's in its binary representation (in ascending order).
# If two integers have the same number of 1's in their binary representation,
# their relative order should be the same as in the original array.

# Example:
# [1,2,4,3] == solution([1,2,3,4])

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1] ==
# solution([0, 0, 0, 1, 0, 1, 1, 0, -1, 1, -1, 0, 1, 0, -1, 1, 0, 0, -1, 1])

# [0, 0, 0, 2, 2, 1, 2, -2, -2, -1, -1] == solution([0, 2, 0, 2, -1, -1, 0, -2, -2, 1, 2])

def solution_wrong(sec):
    in_bin_pos = [bin(k) for k in sec if k >= 0]
    in_bin_neg = [bin(k) for k in sec if k < 0]
    in_bin_pos.sort()
    in_bin_neg.sort()
    return [int(k, 2) for k in in_bin_pos] + [int(k, 2) for k in in_bin_neg]


def solution_still_wrong(array):
    return sorted(array, key=lambda x: (list(str(bin(x))).count('1'), array.index(x)))
