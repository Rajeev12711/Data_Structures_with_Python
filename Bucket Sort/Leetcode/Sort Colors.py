def sortColors(nums):

    count = [0] * (max(nums) + 1)
    for i in nums:
        count[i] += 1

    i = 0
    for j in range(len(count)):
        for k in range(count[j]):
            nums[i] = j
            i += 1
    return nums

print(sortColors([1,2, 0, 2, 2, 0, 1, 1,0]))