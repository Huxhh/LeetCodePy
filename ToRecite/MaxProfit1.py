# coding=utf-8
# author huxh
# time 2020/8/2 4:48 PM


class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        res = 0
        mins = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - mins)
            mins = min(prices[i], mins)
        return res


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        len_prices = len(prices)
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0

        for i in range(1, len_prices):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return max(sell1, sell2)
