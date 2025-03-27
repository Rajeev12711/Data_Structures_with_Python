def duplicate_remove(nums):
    for i in nums:
        if nums.count(i) > 2:
            for z in range(nums.count(i) - 2):
                nums.remove(i)
    return len(nums)

box = [0,0,1,1,1,2,2,3,3,4]

print(duplicate_remove(box))