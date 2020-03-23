# coding=utf-8
# author huxh
# time 2020/3/21 10:29 AM


# O(mn) O(mn)  DFS与BFS
class Solution(object):
    def movingCount(self, m, n, k):
        grid = [[0] * n for _ in range(m)]
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = []
        q.append((0, 0))
        grid[0][0] = 1
        res = 0
        while q:
            i, j = q.pop(0)
            res += 1
            for di, dj in d:
                x = i + di
                y = j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and self.digitsum(x) + self.digitsum(y) <= k:
                    grid[x][y] = 1
                    q.append((x, y))
        return res

    def movingCount2(self, m, n, k):
        grid = [[0] * n for _ in range(m)]
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(i, j):
            res = 1
            grid[i][j] = 1
            for di, dj in d:
                x = i + di
                y = j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and self.digitsum(x) + self.digitsum(y) <= k:
                    res += dfs(x, y)
            return res
        return dfs(0, 0)


    def digitsum(self, x):
        res = 0
        while x:
            res += x % 10
            x //= 10
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(3, 2, 17))