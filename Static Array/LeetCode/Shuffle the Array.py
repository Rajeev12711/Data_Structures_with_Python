def shuffle_array(nums,  n):
    org = nums[:]
    k = 0
    for i in range(0, len(nums)):
        if i%2 == 0:
            nums[i] = org[i - k]
            k+=1
        else:
            nums[i] = org[n]
            n += 1
    return nums


box = [1, 2, 3, 4, 4, 3, 2, 1]
num = int(input("Enter the half of array length: \n"))

print(shuffle_array(box, num))