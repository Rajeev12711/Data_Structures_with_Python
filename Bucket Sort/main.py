def bucketSort(nums):
    if not nums:
        return nums
    counts = [0] * (max(nums)+1)


    for n in nums:
        counts[n] += 1


    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            nums[i] = n
            i += 1
    return nums