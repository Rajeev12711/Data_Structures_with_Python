def shuffle_array(nums,  n):
#     org = nums[:]
#     k = 0
#     for i in range(0, len(nums)):
#         if i%2 == 0:
#             nums[i] = org[i - k]
#             k+=1
#         else:
#             nums[i] = org[n]
#             n += 1
#     return nums

# # 2
#     ans = []
#     for i in range(len(nums)//2):
#         ans.append(nums[i])
#         ans.append(nums[i+n])
#     return ans

# 3
    i = 0
    while i < n:
        nums.append(nums[i])
        nums.append(nums[i + n])
        i += 1
    return nums[-2 * n:]


box = [1, 2, 3, 4, 4, 3, 2, 1]
num = 4

print(shuffle_array(box, num))