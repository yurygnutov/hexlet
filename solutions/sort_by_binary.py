__author__ = 'yury'

# Sort an array of integers by the number of 1's in its binary representation (in ascending order).
# If two integers have the same number of 1's in their binary representation,
# their relative order should be the same as in the original array.

# Example:
# [1,2,4,3] == solution([1,2,3,4])

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1] ==
# solution([0, 0, 0, 1, 0, 1, 1, 0, -1, 1, -1, 0, 1, 0, -1, 1, 0, 0, -1, 1])

# [0, 0, 0, 2, 2, 1, 2, -2, -2, -1, -1] == solution([0, 2, 0, 2, -1, -1, 0, -2, -2, 1, 2])

# Tip: https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%B4_(%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%B0)

def solution_wrong(sec):
    in_bin_pos = [bin(k) for k in sec if k >= 0]
    in_bin_neg = [bin(k) for k in sec if k < 0]
    in_bin_pos.sort()
    in_bin_neg.sort()
    return [int(k, 2) for k in in_bin_pos] + [int(k, 2) for k in in_bin_neg]


def solution_still_wrong(array):
    return sorted(array, key=lambda x: (list(str(bin(x))).count('1'), array.index(x)))


def to_bin(x):
    if x < 0:
        x += (1 << 8)
    formatstring = '{:0%ib}' % 8
    return formatstring.format(x)


def solution(array):
    return sorted(array, key=lambda x: (list(to_bin(x)).count('1'), array.index(x)))
