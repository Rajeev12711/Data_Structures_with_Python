def searchMatrix(matrix, target):

    m, n = len(matrix), len(matrix[0])

    l, r = 0, (m * n) - 1
    while l <= r:
        mid = (l + r) // 2
        mid2 = matrix[mid // n][mid % n]

        if target < mid2:
            r = mid - 1
        elif target > mid2:
            l = mid + 1
        else:
            return True
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 5))