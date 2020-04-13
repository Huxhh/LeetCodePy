# coding=utf-8
# author huxh
# time 2020/4/4 10:23 PM


class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            t = self.com(i)
            if t not in d:
                d[t] = []
            d[t].append(i)

        res = 0
        m = 0
        for k in d:
            m = max(m, len(d[k]))
        for k in d:
            if len(d[k]) == m:
                res += 1
        return res

    def com(self, n):
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res


def canConstruct(s, k):
    from collections import Counter
    if len(s) == k:
        return True

    if len(s) < k:
        return False

    c = Counter(s)
    for t in c:
        if c[t] & 1:
            k -= 1

    if k < 0:
        return False
    return True


class Solution2:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        for a in range(x1, x2 + 1):
            for b in range(y1, y2 + 1):
                if (a - x_center) ** 2 + (b - y_center) ** 2 - radius ** 2 <= 0:
                    return True
        return False


def maxSatisfaction(satisfaction):
    if max(satisfaction) <= 0:
        return 0
    res = 0
    if min(satisfaction) >= 0:
        satisfaction = sorted(satisfaction)
        for i in range(len(satisfaction)):
            res += (i + 1) * satisfaction[i]
        return res

    s = 0
    for a in satisfaction:
        if a >= 0:
            s += a

    newsa = sorted(satisfaction)
    i = 0
    while sum(newsa) <= 0:
        newsa = newsa[1:]
    res = 0
    for i in range(len(newsa)):
        res += (i + 1) * newsa[i]
    return res


if __name__ == '__main__':
    # s = Solution()
    # print(s.countLargestGroup(38))
    print(maxSatisfaction([-5,-7,8,-2,1,3,9,5,-10,4,-5,-2,-1,-6]))