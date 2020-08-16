# coding=utf-8
# author huxh
# time 2020/8/2 10:41 AM


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [99999] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] == 99999 else dp[amount]


def fib(n):
    if n == 2 or n == 1:
        return 1

    pre = 1
    cur = 1
    for i in range(3, n + 1):
        s = pre + cur
        pre = cur
        cur = s
    return cur
