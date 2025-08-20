def move_zeroes(nums):
    k=0
    for i in range(0, len(nums), ):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return nums

def move_zeroe(nums):
    # for i in range(0, len(nums)):
    #     if nums[i]==0:
    #         nums.append(nums[i])
    #         nums.remove(nums[i])
    # return nums
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for k in range(j, n):
        nums[k] = 0
    return nums


box = [0, 1, 0, 3, 12]

print(move_zeroes(box))