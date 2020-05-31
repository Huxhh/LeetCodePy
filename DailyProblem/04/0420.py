# coding=utf-8
# author huxh
# time 2020/4/20 11:07 AM


def numIslands(grid):
    vis = [[0] * len(grid[0]) for _ in range(len(grid))]
    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    ans = 0

    def dfs(i, j):
        vis[i][j] = 1
        for di in d:
            x = i + di[0]
            y = j + di[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not vis[x][y] and grid[x][y] == '1':
                dfs(x, y)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not vis[i][j] and grid[i][j] == '1':
                ans += 1
                dfs(i, j)
    return ans


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        cnt = 0
        n = len(grid)
        m = len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] = '0'
                    q.append((i, j))
                    while q:
                        a, b = q.pop()
                        for s, k in ((a, b + 1), (a + 1, b), (a - 1, b), (a, b - 1)):
                            if 0 <= s < n and 0 <= k < m and grid[s][k] == '1':
                                q.append((s, k))
                                grid[s][k] = '0'

        return cnt


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()


if __name__ == '__main__':
    print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
