__author__ = 'yury'

# Find the largest element in the Syracuse sequence.

# Example:
# 16 == solution(6)

def syracuse(n):
    return n / 2 if not n % 2 else 3 * n + 1


def solution(a):
    m = [a, ]
    while a > 1:
        a = syracuse(a)
        m.append(a)
    return max(m)
