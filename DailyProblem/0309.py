# coding=utf-8

def maxProfit(prices):
    if not prices:
        return 0

    p = 0
    minp = prices[0]
    for i in range(1, len(prices)):
        p = max(p, prices[i] - minp)
        minp = min(minp, prices[i])

    return p