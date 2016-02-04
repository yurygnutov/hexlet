__author__ = 'yury'

# Return the N'th item in the Fibonacci sequence. Hint: The first item in the sequence is 0.

# Example:
# 13 == solution(7)

def solution(num):
    if num < 2:
        return num
    return solution(num - 1) + solution(num - 2)
