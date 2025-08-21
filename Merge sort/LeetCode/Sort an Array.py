def sortArray(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1

    if left < right:
        mid = (left + right) // 2
        sortArray(nums, left, mid)
        sortArray(nums, mid + 1, right)
        merge(nums, left, mid, right)

    return nums


def merge(nums, left, mid, right):
    l = nums[left:mid + 1]
    r = nums[mid + 1:right + 1]

    i = j = 0
    k = left
    ll = len(l)
    lr = len(r)
    while i < ll and j < lr:
        if l[i] <= r[j]:
            nums[k] = l[i]
            i += 1
        else:
            nums[k] = r[j]
            j += 1
        k += 1

    while i < ll:
        nums[k] = l[i]
        i += 1
        k += 1

    while j < lr:
        nums[k] = r[j]
        j += 1
        k += 1


arr = [2,3,7,9,8,9,1,4]
print(sortArray(arr))