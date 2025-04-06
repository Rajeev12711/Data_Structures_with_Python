def median(nums1, nums2):
    nums = nums1[:] + nums2[:]
    nums.sort()
    if len(nums) % 2 != 0:
        return nums[(len(nums)) / 2]
    else:
        mid1 = nums[(len(nums) // 2) - 1]
        mid2 = nums[len(nums) // 2]
        return float(mid1 + mid2)/2

num1 = [1,2]
num2 =[3,4]
print(median(num1, num2))