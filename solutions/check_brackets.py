__author__ = 'yury'

# Check the balance of the brackets in the expression.
# Brackets can be round: "()", square: "[]", curly "{}" and angle: "<>".

# Example:
# false == solution("( {) } ")

def solution(s):
    pairs = {'(': ')', '{': '}', '[': ']', '<': '>',
             ')': '(', '}': '{', ']': '[', '>': '<'}
    s = [b for b in s if b != " "]
    for b in s:
        if s.count(b) != s.count(pairs[b]):
            return False
    return True
