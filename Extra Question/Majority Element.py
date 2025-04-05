def majority(nums):
    # O(n) Space
    # my_dict = {}
    # for i in nums:
    #     if i not in my_dict:
    #         my_dict[i] = nums.count(i)
    # return max(my_dict, key=my_dict.get)


    # O(1) Space
    nums.sort()
    return nums[len(nums)/2]

num=[-1,1,1,1,2,1]
print(majority(num))
