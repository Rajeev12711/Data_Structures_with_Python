def insertion_recursion(nums, index=1):
    if index == len(nums):
        return

    j = index
    while j>0 and nums[j-1] > nums[j]:
        nums[j-1],nums[j] = nums[j], nums[j-1]
        j -= 1
    insertion_recursion(nums, index+1)

    return nums

def insertion_iteration_dec(nums):
    for i in range(1,len(nums)):
        j = i
        while j>0 and nums[j] > nums[j-1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums




print(insertion_iteration_dec(nums=[3,4,5,6,7,1,9, 2]))
print(insertion_recursion(nums=[3,4,5,6,7,1,1, 2]))