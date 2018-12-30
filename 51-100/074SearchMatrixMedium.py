# coding=utf-8

"""
思路：
可以转换为二分查找，即将矩阵假想为一个一位数组，然后使用二分查找
"""

def searchMatrix(matrix, target):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[mid // cols][mid % cols] < target:
            left = mid + 1
        elif matrix[mid // cols][mid % cols] > target:
            right = mid - 1
        else:
            return True

    return False


if __name__ == '__main__':
    matrix = [
                  [1,   3,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 50]
                ]
    print(searchMatrix(matrix, 3))