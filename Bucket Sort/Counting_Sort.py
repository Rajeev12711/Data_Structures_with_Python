def counting(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]


    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

nums = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting(nums)
print("Sorted array:", sorted_arr)