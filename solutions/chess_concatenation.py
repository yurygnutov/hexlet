__author__ = 'yury'

# Concatenate 2 strings by characters, one by one.
# In other words, take the 1st char from the first string,
# then 1st char from the second string,
# then 2nd char from the first string,
# then 2nd char from the second string, and so on.
# If one string ends before the other,
# just continue with the remaining characters.

# Example:
# "awbxcydz" == solution("abcd", "wxyz")

def solution1(one, sec):
    m = []
    one = list(one)
    sec = list(sec)
    for _ in range(sum([len(one), len(sec)])):
        try:
            m.append(one.pop(0))
            m.append(sec.pop(0))
        except:
            m.append("".join(one) or "".join(sec))
            break
    return "".join(m)


def solution2(one, sec):
    ok = ""
    if len(one) != len(sec):
        ok = one[len(sec) % len(one):] if len(one) > len(sec) else sec[len(one) % len(sec):]
    return "".join(["".join(k) for k in zip(one, sec)]) + ok


def solution(o, s):
    result = "".join(["".join(k) for k in zip(o, s)])
    if len(o) == len(s):
        return result
    diff = s[len(o) % len(s):] if len(o) < len(s) else o[len(s) % len(o):]
    return result + diff
