__author__ = 'yury'

# For each element X of the given array, count how many elements to the right of X are smaller than X.
# The last value is always zero since there are no elements to the right of the last element.

# Example: [6,1,1,1,0,1,0] == solution([12,1,2,3,0,11,4])

def solution(sec):
    result = []
    for i, k in enumerate(sec):
        m = sum([1 for v in sec[i:] if v < k])
        result.append(m)
    return result
