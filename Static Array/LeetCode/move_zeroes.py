def move_zeroes(nums):
    k=0
    for i in range(0, len(nums), ):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return nums


box = [0, 1, 0, 3, 12]

print(move_zeroes(box))