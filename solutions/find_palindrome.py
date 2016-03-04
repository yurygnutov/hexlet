__author__ = 'yury'

# A palindrome is a string that is written the same forward as it is in reverse.
# Write a method to return the longest palindrome in a given string.

# Example: "yzzy" == solution("xyzzy")

import itertools

def is_palindrome(x):
    return x == x[::-1]


def split_subsequences(iterable, length=2, overlap=0):
    it = iter(iterable)
    results = list(itertools.islice(it, length))
    while len(results) == length:
        yield results
        results = results[length - overlap:]
        results.extend(itertools.islice(it, length - overlap))
    if results:
        yield results


def solution(t):
    for k in range(len(t), 0, -1):
        for word in split_subsequences(t, k, k - 1):
            if is_palindrome("".join(word)):
                return "".join(word)
