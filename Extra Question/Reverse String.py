strs =["h","e","l","l","o"]
def reverser_list(s):
    size = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[size] = s[size], s[i]
        size -= 1
    return s
    # return s.reverse()

print(reverser_list(strs))