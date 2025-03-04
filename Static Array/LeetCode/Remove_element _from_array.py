def remove_element_from_array(nums, val):
    temp = []
    for i in range(len(nums)):
        if val is nums[i]:
            nums[i] = nums[i]
        else:
            temp.append(nums[i])
    for n in range(len(temp)):
        nums[n] = temp[n]
    return len(temp)


box =[0,1,2,2,3,0,4,2]
enter = 2

print(remove_element_from_array(box, enter))