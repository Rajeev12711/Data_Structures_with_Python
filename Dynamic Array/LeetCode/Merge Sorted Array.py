def merge(nums1, m, nums2, n):
    for i in range(m, m + n):
        nums1[i] = nums2[n - 1]
        n -= 1
    nums1.sort()
    return nums1

num1= [1,2,3,0,0,0]
m1=3
num2= [2,5,6]
n1=3

print(merge(num1, m1, num2, n1))