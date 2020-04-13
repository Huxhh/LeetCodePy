# coding=utf-8
# author huxh
# time 2020/4/13 12:31 PM


def maxProfit(prices):
    if not prices:
        return 0

    res = 0
    mins = prices[0]
    for i in range(1, len(prices)):
        res = max(res, prices[i] - mins)
        mins = min(mins, prices[i])
    return res
