def sortColors(nums):

    count0 = count1 = count2 = 0

    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(count0):
        nums[i] = 0
    for i in range(count0, count0 + count1):
        nums[i] = 1
    for i in range(count0 + count1, len(nums)):
        nums[i] = 2

    return nums

print(sortColors([1,2, 0, 2, 2, 0, 1, 1,0]))