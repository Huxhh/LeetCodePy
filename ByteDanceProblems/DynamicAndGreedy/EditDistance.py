# coding=utf-8

def editDistance(word1, word2):
    n1 = len(word1) + 1
    n2 = len(word2) + 1
    dp = []
    for i in range(n1):
        dp.append([99999] * n2)

    for i in range(n1):
        dp[i][0] = i
    for i in range(n2):
        dp[0][i] = i

    for i in range(1, n1):
        for j in range(1, n2):
            # flag = 0 if word1[i - 1] == word2[j - 1] else flag = 1
            if word1[i - 1] == word2[j - 1]:
                flag = 0
            else:
                flag = 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + flag)

    return dp[-1][-1]
