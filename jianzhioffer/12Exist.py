# coding=utf-8
# author huxh
# time 2020/3/20 4:16 PM

# O(3^K MN) O(K)  **
def exist(board, word):
    if not board or not word:
        return False

    def dfs(i, j, word, board, visited):
        if not word:
            return True
        visited[i][j] = 1
        ans = False
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in d:
            x = i + dx
            y = j + dy
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[0] and not visited[x][y]:
                ans = ans or dfs(x, y, word[1:], board, visited)
        visited[i][j] = 0
        return ans

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                visited = [[0] * len(board[0]) for _ in range(len(board))]
                if dfs(i, j, word[1:], board, visited):
                    return True

    return False
