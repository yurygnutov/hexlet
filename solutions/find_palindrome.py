__author__ = 'yury'

# A palindrome is a string that is written the same forward as it is in reverse.
# Write a method to return the longest palindrome in a given string.

# Example: "yzzy" == solution("xyzzy")


def is_palindrome(x):
    return x == x[::-1]


def each_cons(x, size):
    return [x[i:i+size] for i in range(len(x)-size+1)]


def solution(t):
    for k in range(len(t), 0, -1):
        for word in each_cons(t, k):
            if is_palindrome("".join(word)):
                return "".join(word)
