def remove_duplicates(nums):
    # l = []
    # for i in range(0, len(nums)):
    #     if nums[i] not in l:
    #         l.append(nums[i])
    # nums = l[:]
    # print(nums)
    # return len(l)

    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1


box = [0,0,1,1,1,2,2,3,3,4]

print(remove_duplicates(box))
