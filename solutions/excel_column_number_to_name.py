__author__ = 'yury'

# Given a positive integer,
# return its corresponding column title as it appears in an Excel sheet.
# For example: 1 -> A, 2 -> B, 3 -> C, ..., 26 -> Z, 27 -> AA, 28 -> AB
# Example:
# "YP" == solution(666)

def solution(column_number):
    name = []
    while column_number > 0:
        mod = (column_number - 1) % 26
        name.append(chr(65 + mod))  # chr(65) == 'A'
        column_number = int((column_number - mod) / 26)
    return "".join(name[::-1])
