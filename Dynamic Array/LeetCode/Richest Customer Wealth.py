def wealth(nums):
    add = []
    for i in range(0, len(nums)):
        add.append(sum(nums[i]))
    return max(add)


box = [[1,5],[7,3],[3,5]]
print(wealth(box))