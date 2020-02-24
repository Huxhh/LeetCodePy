# coding=utf-8
import heapq

def countNegatives(grid):
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])
    res = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] < 0:
                res +=1
    return res


class ProductOfNumbers(object):

    def __init__(self):
        self.nums = []
        self.muls = []
        self.index = 0

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.nums:
            self.nums.append(num)
            self.muls.append(num)
        else:
            self.nums.append(num)
            self.muls.append(num)
            if num == 0:
                self.muls = [0] * len(self.muls)
                self.index = len(self.nums) - 1
                return
            if num == 1:
                return
            for i in range(self.index, len(self.muls) - 1):
                self.muls[i] *= num


    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        return self.muls[-k]


def maxEvents(events):
    if not events:
        return 0
    #
    # events = sorted(events, key=lambda event:event[0])
    # events = sorted(events, key=lambda event:event[1])
    days = [0] * 100001
    res = 0
    for event in events:
        for i in range(event[0], event[1] + 1):
            if days[i] == 0:
                days[i] = 1
                res += 1
                break
    return res


def maxEvents2(events):
    if not events:
        return 0

    events = sorted(events, key=lambda event:event[0])
    events = sorted(events, key=lambda event:event[1])
    days = [0] * (events[-1][1] + 1)
    res = 0
    for i in range(len(days)):
        for event in events:
            if event[0] <= i <= event[1]:
                res += 1
                events.remove(event)
                break
    return res


class Solution:
    def maxEvents(self, events):
        ans = 0
        end = list()
        events = sorted(events)
        for i in range(1, 100010):
            while events and events[0][0] == i:
                heapq.heappush(end, events.pop(0)[1])
            while end and end[0] < i:
                heapq.heappop(end)
            if end:
                heapq.heappop(end)
                ans += 1
        return ans



if __name__ == '__main__':
    # p = ProductOfNumbers()
    # p.add(3)
    # p.add(0)
    # p.add(2)
    # p.add(5)
    # p.add(4)
    # print(p.getProduct(2))
    # # print(p.getProduct(3))
    # # print(p.getProduct(4))
    events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    print(maxEvents2(events))