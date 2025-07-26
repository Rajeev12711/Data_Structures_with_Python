def checker(heights):
    count = 0
    expected = sorted(heights[:])

    # for i in range(1, len(heights)):
    #     j = i
    #     while j >0 and expected[j] < expected[j-1]:
    #         expected[j], expected[j-1] =  expected[j-1], expected[j]
    #         j -=1

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1

    return count

print(checker([5,3,6,2,1,1,9]))