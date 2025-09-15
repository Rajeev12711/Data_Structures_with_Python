def searchInsert(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0
        elif target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
    return l

print(searchInsert([1,3,5,6],2))