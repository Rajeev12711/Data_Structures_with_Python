def altitude(nums):
    arr=[0]
    k=0
    for i in range(0, len(nums)):
        arr.append(arr[k] + nums[i])
        k+=1
    return max(arr)

box = [-5,1,5,0,-7]

print(altitude(box))