__author__ = 'yury'

# Check if a given pair of numbers is a Ruth–Aaron pair.
# A Ruth–Aaron pair consists of two consecutive integers (e.g. 714 and 715)
# for which the sums of the prime factors of each integer are equal.
# When calculating the sum, take into account the repeating factors.

# Example:
# true == solution([8,9])


def pf(n):
    pf = []
    d = 2
    while d ** 2 <= n:
        while (n % d) == 0:
            pf.append(d)
            n //= d
        d += 1
    if n > 1:
       pf.append(n)
    return pf

def solution(pair):
    return sum(pf(pair[0])) == sum(pf(pair[1]))
