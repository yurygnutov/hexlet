__author__ = 'yury'

# Return the sum of all prime numbers from 2 up to a given number.

# Example:
# 4227 == solution(200)

def is_prime(a):
    return all(a % i for i in range(2, a))


def solution(n):
    return sum([j for j in range(2, n) if is_prime(j)])
