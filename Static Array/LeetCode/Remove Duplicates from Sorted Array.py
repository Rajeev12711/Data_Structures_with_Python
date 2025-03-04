def remove_duplicates(nums):
    l = []
    for i in range(0, len(nums)):
        if nums[i] not in l:
            l.append(nums[i])
    nums = l[:]
    print(nums)
    return len(l)


box = [0,0,1,1,1,2,2,3,3,4]

print(remove_duplicates(box))
