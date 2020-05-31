# coding=utf-8
# author huxh
# time 2020/3/26 9:54 AM


def numRookCaptures(board):
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = [0]

    def dfs(x, y, di):
        if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
            return
        if board[x][y] == 'B':
            return
        if board[x][y] == 'p':
            ans[0] += 1
            return
        if di == 0:
            for i in range(len(d)):
                dx = d[i][0] + x
                dy = d[i][1] + y
                dfs(dx, dy, i + 1)

        else:
            dfs(x + d[di - 1][0], y + d[di - 1][1], di)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                dfs(i, j, 0)
    return ans[0]

