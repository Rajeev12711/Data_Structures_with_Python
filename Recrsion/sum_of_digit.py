def digit(n):
    n = abs(n)
    if n==0:
        return 0
    return (n%10)+digit(n//10)


print(digit(-127))