def apply_operations_to_array(nums):
    # k=0
    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         nums[i] = nums[i]*2
    #         nums[i+1] = 0
    #
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[i], nums[k] = nums[k], nums[i]
    #         k+=1
    # print(nums)

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    nums1 = [i for i in nums if i != 0]
    zeros = [0] * (len(nums) - len(nums1))
    nums = nums1 + zeros
    return nums


box =[1,2,2,1,1,0]
print(apply_operations_to_array(box))