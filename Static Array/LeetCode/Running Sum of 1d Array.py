def running_sum(nums):
    res = 0
    for i in range(len(nums)):
        res = res + nums[i]
        nums[i] = res
    return nums

box = [3,1,2,10,1]
print(running_sum(box))
