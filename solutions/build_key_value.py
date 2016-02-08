__author__ = 'yury'

# Flatten the given hash. This is how HTTP libraries pack data when POST requests are made
# using x-www-form-urlencoded.

# Example: {"x[0]":"1","x[1]":"2","x[2]":"3"} == solution({"x":["1","2","3"]})

def solution(inp, key=""):
    result = {}
    if not isinstance(inp, (dict, list)):
        return {key: inp}
    elif isinstance(inp, dict):
        for k, v in inp.items():
            newkey = "%s[%s]" % (str(key), str(k)) if key else str(k)
            fv = solution(v, newkey)
            if isinstance(fv, dict):
                for n, m in fv.items():
                    result[n] = m
    elif isinstance(inp, list):
        for i, v in enumerate(inp):
            newkey = "%s[%d]" % (key, i) if key else None
            if newkey:
                fv = solution(v, newkey)
                if isinstance(fv, dict):
                    for n, m in fv.items():
                        result[n] = m
    return result
