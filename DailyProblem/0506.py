# coding=utf-8
# author huxh
# time 2020/5/6 10:04 AM


def mincostTickets(days, costs):
    n = len(days)
    durations = [1,7,30]
    mem = {}

    def dp(i):
        if i in mem:
            return mem[i]
        if i >= n:
            return 0
        ans = 10 ** 9
        j = i
        for c, d in zip(costs, durations):
            while j < n and days[j] < days[i] + d:
                j += 1
            ans = min(ans, dp(j) + c)
        mem[i] = ans
        return ans

    return dp(0)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]  # dp数组，每个元素代表到当前天数最少钱数，为下标方便对应，多加一个 0 位置
        days_idx = 0  # 设定一个days指标，标记应该处理 days 数组中哪一个元素
        for i in range(1, len(dp)):
            if i != days[days_idx]:  # 若当前天数不是待处理天数，则其花费费用和前一天相同
                dp[i] = dp[i - 1]
            else:
                # 若 i 走到了待处理天数，则从三种方式中选一个最小的
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        return dp[-1]  # 返回最后一天对应的费用即可
