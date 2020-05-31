# coding=utf-8
# author huxh
# time 2020/4/23 10:28 AM


class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod


if __name__ == '__main__':
    s = Solution()
    print(s.waysToChange(10))
