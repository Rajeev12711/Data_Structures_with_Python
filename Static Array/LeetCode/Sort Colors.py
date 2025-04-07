def color(nums):
    red = nums.count(0)
    white = nums.count(1)
    blue = nums.count(2)
    for i in range(len(nums)):
        if red != 0:
            nums[i] = 0
            red -= 1
        elif white != 0:
            nums[i] = 1
            white -= 1
        elif blue != 0:
            nums[i] = 2
            blue -= 1
    return nums


num = [2,0,2,1,1,0]
print(color(num))