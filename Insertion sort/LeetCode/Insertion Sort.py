# https://neetcode.io/problems/insertionSort
# Question Link

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key}, "{self.value}")'

class Solution:
    def insertionSort(self, pairs):
        result = [pairs[:]]

        for i in range(1, len(pairs)):
            j = i
            while j > 0 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            result.append(pairs[:])

        return result

pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
solution = Solution()
snapshots = solution.insertionSort(pairs)

for step in snapshots:
    print(step)

