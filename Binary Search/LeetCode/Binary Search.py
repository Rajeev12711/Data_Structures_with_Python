def binarySearch(nums, target):
    l, r = 0 , len(nums)-1

    while l <= r:
        mid = (l+r)//2

        if target < nums[mid]:
            r = mid-1
        elif target > nums[mid]:
            l = mid +1
        else:
            return mid
    return -1

print(binarySearch([1, 3, 3, 4, 5, 6, 7, 8], 3))