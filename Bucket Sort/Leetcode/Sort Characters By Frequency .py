def frequencySort(s):
    box = {}

    for ch in s:
        box[ch] = box.get(ch, 0) + 1

    result = ""
    for i in range(len(box)):
        ch = max(box, key=box.get)
        count = box.pop(ch)

        result += (ch * count)

    return result

print(frequencySort("tree"))