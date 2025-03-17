def valid_parentheses(s):
    res = []
    sets={')':'(', '}':'{', ']':'['}
    for c in s:
        if c not in sets:
            res.append(c)
        elif c in sets:
            if not res and res[-1] != sets[c]:
                return False
            res.pop()

    return res==[]


box="([])"
print(valid_parentheses(box))