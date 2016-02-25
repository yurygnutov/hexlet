import re

__author__ = 'yury'


# Given a sentence, sort characters in each word alphabetically.

# Example:
# "Eey fo Entw, adn Eot fo Fgor, Loow fo Abt, adn Egnotu fo Dgo." ==
# solution("Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog.")


def myfancysortfunction(w):
    word = w.group(0)
    word = "".join(sorted(word.lower()))
    if [k for k in w.group(0) if k.isupper()]:
        word = word.capitalize()
    return word

def solution(s):
    return re.sub('\w+', myfancysortfunction, s)