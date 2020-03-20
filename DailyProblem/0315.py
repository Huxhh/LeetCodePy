# coding=utf-8

class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        r = len(grid)
        c = len(grid[0])
        visited = [[0] * c for _ in range(r)]
        d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(i, j):
            tmp = 1
            visited[i][j] = 1
            for x, y in d:
                di, dj = i + x, j + y
                if 0 <= di < r and 0 <= dj < c and grid[di][dj] == 1 and not visited[di][dj]:
                    tmp += dfs(di, dj)
            return tmp

        maxs = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxs = max(maxs, dfs(i, j))

        return maxs