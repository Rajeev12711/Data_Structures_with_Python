def topKFrequent(nums, k):

    bucket = {}
    for num in nums:
        bucket[num] = bucket.get(num, 0) + 1

    result = []
    for i in range(k):
        index = max(bucket, key=bucket.get)
        result.append(index)
        bucket[index] = 0
    return result

print(topKFrequent([1,1,1,2,2,3],2))