
def searchRange(nums, target):

    l = search(nums, target, True)
    r = search(nums, target, False)
    return [l, r]


def search(nums, target, left):
    l, r = 0, len(nums) - 1
    i = -1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            i = mid
            if left:
                r = mid - 1
            else:
                l = mid + 1
    return i

print(searchRange([5,7,7,8,8,10], 8))