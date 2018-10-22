# coding=utf-8

"""
思路
首先将矩阵按行反序，然后再沿着对角线交换，如下：
 1 2 3     7 8 9     7 4 1
 4 5 6  => 4 5 6  => 8 5 2
 7 8 9     1 2 3     9 6 3
"""

def rotate(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix


if __name__ == '__main__':
    matrix = [
                  [15,13, 2, 5],
                  [14, 3, 4, 1],
                  [12, 6, 8, 9],
                  [16, 7,10,11]
             ]

    matrix.reverse()
    print(matrix)