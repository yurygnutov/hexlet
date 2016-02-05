__author__ = 'yury'

# Given a sentence and a word, find all the positions in which the word occurs in the sentence.
# Return an array of such positions.

# Example:
# [12] == solution("find a word in some sentence", "in")


def solution(s, w):
    result, chop, seq = [], [], s.split()
    while seq:
        if w == seq[0]:
            result.append(len(" ".join(chop + [" ", ])) - 1)
        chop.append(seq.pop(0))
    return result
