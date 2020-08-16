# coding=utf-8
# author huxh
# time 2020/8/2 11:57 AM

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(dp[0])):
            dp[0][i] = i

        for i in range(len(dp)):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                flag = 1
                if word1[i - 1] == word2[j - 1]:
                    flag = 0
                dp[i][j] = min(dp[i - 1][j - 1] + flag, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]
