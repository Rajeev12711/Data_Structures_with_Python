def contains(nums):
    seen = set(nums)

    return len(nums) != len(seen)

num= [1,2,3,1]
print(contains(num))