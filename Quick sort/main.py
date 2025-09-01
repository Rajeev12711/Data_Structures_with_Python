def quickSort(nums, s=0, e=None):
    if e is None:
        e = len(nums) - 1

    if s >= e:
        return

    pivot = nums[e]
    low = s

    for i in range(s, e):
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1

    nums[low], nums[e] = nums[e], nums[low]

    quickSort(nums, s, low - 1)
    quickSort(nums, low + 1, e)

    return nums

arr = [10, 7, 8, 9, 1, 5]
print(quickSort(arr))