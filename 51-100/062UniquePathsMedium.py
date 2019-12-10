# coding=utf-8

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.record = [[0] * n for i in range(m)]
        self.record[0][0] = 1
        return self.dfs(m - 1, n - 1)

    def dfs(self, m, n):
        if m < 0 or n < 0:
            return 0
        if m == 0 or n == 0:
            return 1
        if self.record[m][n] > 0:
            return self.record[m][n]
        self.record[m][n] = self.dfs(m - 1, n) + self.dfs(m, n - 1)
        return self.record[m][n]


def uniquePaths(m, n):
    record = [0] * n
    record[0] = 1
    for i in range(m):
        for j in range(1, n):
            record[j] += record[j - 1]
    return record[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))
    print(uniquePaths(7, 3))
