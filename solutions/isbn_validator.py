__author__ = 'yury'

# Validate given ISBN identifier.
# An ISBN is a ten digit code which identifies a book.
# The first nine digits represent the book and the last digit is used to make sure the ISBN is correct
# To verify an ISBN you obtain the sum of 10 times the first digit,
# 9 times the second digit, 8 times the third digit ...
# all the way till you add 1 times the last.digit.
# if the sum leaves no remainder when divided by 11 the code is valid ISBN.

# Example:
# true == solution("0-684-84328-5")

def solution(isbn):
    isbn = isbn.replace("-", "")
    return sum([int(n) * (len(isbn) - i) for i, n in enumerate(isbn)]) % 11 == 0
