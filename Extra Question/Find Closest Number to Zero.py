def close(nums):
    num = nums[0]

    for i in range(len(nums)):

        if abs(num) > abs(nums[i]) or abs(num) == abs(nums[i]) and num < nums[i]:
            num = nums[i]

    return num

box= [-4,-2,1,4,8]

print(close(box))