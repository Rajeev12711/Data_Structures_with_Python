def palindrome(n):
    n = str(n)
    if len(n) <= 1:
        return True
    elif n[0] != n[-1]:
        return False
    return palindrome(n[1:-1])


print(palindrome(121))