def duplicates_array(nums):
    check = set()
    arr = []
    for i in range(0,  len(nums)):
        if nums[i] not in check:
            check.add(nums[i])
        else:
            arr.append(nums[i])
    return arr





box = [7,3,2,7,8,2,3,4]

print(duplicates_array(box))



