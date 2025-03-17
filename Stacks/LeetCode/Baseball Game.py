def baseball(operations):
    res=[]
    for c in operations:
        if c == "C":
            res.pop()
        elif c == "D":
            res.append(2 *res[-1])
        elif c == '+':
            res.append(res[-2]+res[-1])
        else:
            res.append(int(c))
    return sum(res)

s=["5","-2","4","C","D","9","+","+"]
print(baseball(s))
