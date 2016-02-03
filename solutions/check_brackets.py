__author__ = 'yury'

# Check the balance of the brackets in the expression.
# Brackets can be round: "()", square: "[]", curly "{}" and angle: "<>".

# Example:
# false == solution("( {) } ")

def solution_wrong(s):
    pairs = {'(': ')', '{': '}', '[': ']', '<': '>',
             ')': '(', '}': '{', ']': '[', '>': '<'}
    s = [b for b in s if b != " "]
    for b in s:
        if s.count(b) != s.count(pairs[b]):
            return False
    return True

def solution(s):
    stack = []
    openb, closeb = "<({[", ">)}]"
    for b in s:
        if b in openb:
            stack.append(b)
        elif b in closeb:
            if not stack:
                return False
            stack_close = stack.pop()
            if stack_close != openb[closeb.index(b)]:
                return False
    return stack == []
