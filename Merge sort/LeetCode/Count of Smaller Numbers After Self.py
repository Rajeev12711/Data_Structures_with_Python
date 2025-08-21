from sortedcontainers import SortedList

def countSmaller(nums):
    sortedArr = SortedList([])
    result = []

    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]

        idx = sortedArr.bisect_left(num)
        result.append(idx)
        sortedArr.add(num)
    return result[::-1]


arr = [5,2,6,1]
print(countSmaller(arr))