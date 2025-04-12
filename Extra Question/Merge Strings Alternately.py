def merge_alternately(word1, word2):
    result=""
    i = 0
    if len(word1) <= len(word2):
        size = len(word1)
        for z in range(size):
            result += word1[z]+word2[i]
            i+=1
        result += "".join(word2[i:])
    else:
        size = len(word2)
        for z in range(size):
            result += word1[z]+word2[i]
            i+=1
        result += "".join(word1[i:])
    return result

word_1 = "abcd"
word_2 = "pqrs"

print(merge_alternately(word_1, word_2))