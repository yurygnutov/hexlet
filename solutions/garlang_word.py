__author__ = 'yury'

# Write function that, given a lowercase word,
# returns the degree of the word if it's a garland word and 0 otherwise.
# A garland word is one that starts and ends with the same N letters in the same order,
# for some N greater than 0, but less that the length of the word.

# Example:
# 2 == solution("onion")

def solution(word):
    degree = 0
    for letter in word[:len(word) - 1][::-1]:
        if letter == word[::-1][degree]:
            degree += 1
        else:
            degree = 0
    return degree
