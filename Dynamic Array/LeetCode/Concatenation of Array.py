def concatenation_array(nums):
    arr = nums[:]
    arr = arr + nums
    return arr

box =[1,3,2,1]
print(concatenation_array(box))