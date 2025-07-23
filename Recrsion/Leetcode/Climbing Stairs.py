def climb_stairs(n):
    if n in [0, 1, 2]:
        return n
    else:
        prev1 = 1
        prev2 = 1
        for i in range(2, n + 1):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
        return cur

print(climb_stairs(44))