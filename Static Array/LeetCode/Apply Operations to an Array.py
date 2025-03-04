def apply_operations_to_array(nums):
    k=0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[k] = nums[k], nums[i]
            k+=1
    print(nums)


box =[1,2,2,1,1,0]
apply_operations_to_array(box)