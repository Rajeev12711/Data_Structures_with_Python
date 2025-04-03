val = "1111"
arr = []
for i in range(1, len(val)):
    fir = val[:i].count('0')
    sec = val [i:].count('1')
    arr.append(fir+sec)
print(max(arr))