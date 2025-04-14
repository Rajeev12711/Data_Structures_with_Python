def subsequence(s,t):
    # c = ''
    # j = 0
    # if len(s) == 0:
    #     return True
    # for i in range(0, len(t)):
    #
    #     if t[i] in s[j]:
    #         c += t[i]
    #         j += 1
    #
    #     if s == c:
    #         return True
    #
    # return False

    i= 0
    j=0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


s1 = "abc"
t1 = "ahgdc"

print(subsequence(s1,t1))