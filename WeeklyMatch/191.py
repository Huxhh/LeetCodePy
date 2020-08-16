# coding=utf-8
# author huxh
# time 2020/5/31 10:14 AM


def maxProduct(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res = max(res, (nums[i] - 1) * (nums[j] - 1))
    return res

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        maxw, maxh = 0, 0
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        for i in range(len(horizontalCuts)):
            if i == 0:
                maxh = max(maxh, horizontalCuts[i] - 0)
            else:
                maxh = max(maxh, horizontalCuts[i] - horizontalCuts[i - 1])
        maxh = max(maxh, h - horizontalCuts[-1])
        for i in range(len(verticalCuts)):
            if i == 0:
                maxw = max(maxw, verticalCuts[i] - 0)
            else:
                maxw = max(maxw, verticalCuts[i] - verticalCuts[i - 1])
        maxw = max(maxw, w - verticalCuts[-1])

        return int((maxw * maxh) % (1e9 + 7))


def minReorder(n, connections):
    d = {}
    for con in connections:
        if con[0] not in d:
            d[con[0]] = []
        d[con[0]].append(con[1])

    res = 0
    tmp = set()
    tmp.add(0)
    if 0 in d:
        res += len(d[0])
        for p in d[0]:
            tmp.add(p)

    for k in d:
        if 0 in d[k]:
            tmp.add(k)

    while len(tmp) != n:
        cur = list(tmp)
        for k in cur:
            if k in d:
                for p in d[k]:
                    if p in tmp:
                        continue
                    res += 1
                    tmp.add(p)
        for k in d:
            if k not in tmp:
                for p in d[k]:
                    if p in tmp:
                        tmp.add(k)
                        break

    return res


def getProbability(balls):

    def getres(x):
        res = 1
        while x > 1:
            res *= x
            x -= 1
        return res

    total = 0
    tmp = 1
    for n in balls:
        total += n
        if n != 1:
            tmp *= getres(n)
    all_sit = getres(total) // tmp
    return all_sit






if __name__ == '__main__':
    # print(minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
    print(getProbability([3,2,1]))