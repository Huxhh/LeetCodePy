# coding=utf-8
# author huxh
# time 2020/4/2 9:46 AM


def gameOfLife(board):
    if not board:
        return board

    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    rows = len(board)
    cols = len(board[0])
    newboard = [[board[i][j] for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            tmp = 0
            for di in d:
                x = i + di[0]
                y = j + di[1]
                if 0 <= x < rows and 0 <= y < cols:
                    tmp += newboard[x][y]
            if newboard[i][j] == 1:
                if tmp < 2:
                    board[i][j] = 0
                if tmp > 3:
                    board[i][j] = 0
            else:
                if tmp == 3:
                    board[i][j] = 1


def gameOfLife2(board):
    if not board:
        return board

    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            tmp = 0
            for di in d:
                x = i + di[0]
                y = j + di[1]
                if 0 <= x < rows and 0 <= y < cols and abs(board[x][y]) == 1:
                    tmp += 1
            if board[i][j] == 1:
                if tmp < 2 or tmp > 3:
                    board[i][j] = -1
            if board[i][j] == 0:
                if tmp == 3:
                    board[i][j] = 2

    for i in range(rows):
        for j in range(cols):
            if board[i][j] > 0:
                board[i][j] = 1
            else:
                board[i][j] = 0
