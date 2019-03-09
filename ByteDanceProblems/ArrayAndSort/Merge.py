# coding=utf-8


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    if not intervals:
        return intervals
    intervals.sort(key=lambda x: x.start)
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if res[-1].end < intervals[i].start:
            res.append(intervals[i])
        else:
            res[-1].end = max(intervals[i].end, res[-1].end)

    return res


def merge2(intervals):
    if not intervals:
        return intervals
    res = []
    n = len(intervals)
    starts = [0] * n
    ends = [0] * n
    for i in range(n):
        starts[i] = intervals[i].start
        ends[i] = intervals[i].end
    starts = sorted(starts)
    ends = sorted(ends)
    j = 0
    for i in range(n):
        if i == n - 1 or starts[i + 1] > ends[i]:
            res.append(Interval(starts[j], ends[i]))
            j += 1
    return res

