# coding=utf-8


class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = self.dfs(i, j, rows, cols, grid, 0)
                    maxarea = max(area, maxarea)

        return maxarea

    def dfs(self, i, j, rows, cols, grid, carea):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            return carea

        grid[i][j] = 0
        carea += 1
        carea = self.dfs(i + 1, j, rows, cols, grid, carea)
        carea = self.dfs(i + 1, j, rows, cols, grid, carea)
        carea = self.dfs(i, j + 1, rows, cols, grid, carea)
        carea = self.dfs(i - 1, j, rows, cols, grid, carea)
        carea = self.dfs(i, j - 1, rows, cols, grid, carea)
        return carea


if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    s = Solution()
    print(s.maxAreaOfIsland(grid))
