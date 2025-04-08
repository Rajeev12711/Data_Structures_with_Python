def array_distinct(nums):
    k = 0
    while len(nums) > 0:
        if len(nums) == len(set(nums)):
            return k
        else:
            nums = nums[3:]
            k += 1
    return k

num=[1,2,3,4,2,3,3,5,7]
print(array_distinct(num))
