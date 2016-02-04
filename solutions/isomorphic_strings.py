__author__ = 'yury'

# Given two strings, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.

# Example:
# true == solution("egg", "add")

def solution(a, b):
    if len(a) != len(b):
        return False
    d = {}
    for k, v in zip(a, b):
        if not d.get(k):
            if v in d.values():
                return False
            d[k] = v
        else:
            if d[k] != v:
                return False
    return True

