def mySqrt(x):

    if x <= 1:
        return x

    l, r = 2, x // 2
    while l <= r:
        val = (l + r) // 2
        if val * val == x:
            return val
        elif val * val > x:
            r = val - 1
        else:
            l = val + 1
    return r

print(mySqrt(396))