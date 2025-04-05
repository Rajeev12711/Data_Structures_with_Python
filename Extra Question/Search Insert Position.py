def search_insert(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
            return i
        elif nums[len(nums)-1]<target:
            return len(nums)
        elif target< nums[i]:
            return i


# num=[1,3,5,6]
# targ = 2
num =[1,3,5,6]
targ =7
print(search_insert(num, targ))