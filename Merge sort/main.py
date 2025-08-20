#  Extra Memory
def divide(nums):

    n = len(nums)
    if n<=1:
        return nums

    mid = n//2

    left = divide(nums[:mid])
    right = divide(nums[mid:])

    return conquer(left, right)

def conquer(nums1, nums2):
    i = j = 0
    result = []

    while i < len(nums1) and j <len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j +=1

    result.extend(nums1[i:])
    result.extend(nums2[j:])

    return result


arr = [2,3,7,5,8,9,1,4]
print(divide(arr))

# In place
def sorts(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1

    if left < right:
        mid = (left + right) // 2
        sorts(nums, left, mid)
        sorts(nums, mid + 1, right)
        merge(nums, left, mid, right)
    return nums


def merge(nums, left, mid, right):
    L = nums[left:mid+1]
    R = nums[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1



arr = [2,3,7,9,8,9,1,4]
print(sorts(arr))