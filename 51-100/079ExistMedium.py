# coding=utf-8
# author huxh
# time 2020/9/12 10:34 AM


def exist(board, word):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j, cur, visited):
        if not cur:
            return True

        for di in d:
            ni = i + di[0]
            nj = j + di[1]
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not visited[ni][nj] and board[ni][nj] == cur[0]:
                visited[ni][nj] = 1

                if dfs(ni, nj, cur[1:], visited):
                    return True
                else:
                    visited[ni][nj] = 0
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                visited = [[0] * len(board[0]) for _ in range(len(board))]
                visited[i][j] = 1
                if dfs(i, j, word[1:], visited):
                    return True
    return False
