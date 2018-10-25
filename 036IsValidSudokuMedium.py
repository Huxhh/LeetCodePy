# coding=utf-8


"""
思路
找到存在的数字，查找其所在的行，列，小区域内有没有相同的数字即可
时间复杂度 O(n^2 - n^3) 空间复杂度 O(1)
"""


def isValidSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                nums = board[i][j]
                for k in range(j + 1, 9):
                    if nums == board[i][k]:
                        return False
                for k in range(i + 1, 9):
                    if nums == board[k][j]:
                        return False

                for x in range(3 * (i // 3), 3 * (i // 3 + 1)):
                    for y in range(3 * (j // 3), 3 * (j // 3 + 1)):
                        if board[x][y] == nums and x != i and y != j:
                            return False

    return True


if __name__ == '__main__':
    board = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board))
