# coding=utf-8
# author huxh
# time 2020/3/29 10:29 AM


def findLucky(arr):
    from collections import Counter
    c = Counter(arr)
    res = -1
    for k in c:
        if k == c[k]:
            res = max(res, k)
    return res


def numTeams(rating):
    if not rating:
        return 0

    res = 0
    for i in range(len(rating) - 2):
        for j in range(i + 1, len(rating) - 1):
            for k in range(j + 1, len(rating)):
                if rating[i] < rating[j] < rating[k]:
                    res += 1
                if rating[i] > rating[j] > rating[k]:
                    res += 1
    return res


class UndergroundSystem(object):

    def __init__(self):
        self.d = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if stationName not in self.d:
            self.d[stationName] = {'in': {}, 'out': {}}
        self.d[stationName]['in'][id] = t


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if stationName not in self.d:
            self.d[stationName] = {'in': {}, 'out': {}}
        self.d[stationName]['out'][id] = t


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        total = 0
        cnt = 0
        for sid in self.d[startStation]['in']:
            for eid in self.d[endStation]['out']:
                if sid == eid:
                    total += (self.d[endStation]['out'][eid] - self.d[startStation]['in'][sid])
                    cnt += 1
        if cnt:
            return total * 1.0 / cnt
        return 0


