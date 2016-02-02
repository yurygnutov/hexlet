__author__ = 'yury'

# Find all the anagrams in a vector of words. 
# Your function should return a vector of vectors, 
# where each sub-vector is a group of words which are anagrams of each other. 
# Words without any anagrams should not be included in the result.
# Example: 
# [["veer","ever"],["lake","kale"],["item","mite"]] == solution(["veer","lake","item","kale","mite","ever"])

def solution(words):
    sorted_words = []
    final = []
    for word in words:
        w = list(word)
        w.sort()
        sorted_words.append("".join(w))
    # then we have two lists:
    # ["veer", "lake", "item", "kale", "mite", "ever"]
    # ['eerv', 'aekl', 'eimt', 'aekl', 'eimt', 'eerv']
    for sorted_word in set(sorted_words):
        #  set(['aekl', 'eimt', 'eerv'])
        an = []
        for k, v in zip(words, sorted_words):
            if v == sorted_word and sorted_words.count(v) > 1:
                an.append(k)
        if an:
            final.append(an)
    return final
