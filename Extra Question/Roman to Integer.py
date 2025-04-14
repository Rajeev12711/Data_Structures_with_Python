s = "LVIII"
maps = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
result = 0
for i in range(len(s)-1, -1, -1):
    if i == (len(s) - 1):
        result += maps[s[i]]
    elif maps[s[i]] < maps[s[i + 1]]:
        result = result - maps[s[i]]
    else:
        result = maps[s[i]] + result

print(result)