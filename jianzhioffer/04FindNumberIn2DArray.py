# coding=utf-8


# 时间O(mn) 空间O(1)
def findNumberIn2DArray(matrix, target):
    if not matrix or not matrix[0]:
        return False
    for i in range(len(matrix)):
        if target < matrix[i][0]:
            break
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False

# O(n + m) O(1)   ***
def findNumberIn2DArray2(matrix, target):
    if not matrix or not matrix[0]:
        return False

    r = 0
    c = len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return True
        if matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return False