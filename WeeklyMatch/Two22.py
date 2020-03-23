# coding=utf-8
# author huxh
# time 2020/3/21 10:29 PM


def findTheDistanceValue(arr1, arr2, d):
    res = 0
    for n in arr1:
        f = 0
        for m in arr2:
            if abs(n - m) <= d:
                f = 1
                break
        if f:
            continue
        res += 1
    return res


def maxNumberOfFamilies(n, reservedSeats):
    reservedSeats = sorted(reservedSeats)
    q = []
    res = 2 * n
    for r, c in reservedSeats:
        if not q or r == q[-1][0]:
            q.append((r, c))
            continue
        tmp = []
        while q:
            tmp.append(q.pop()[1])
        s1 = 0
        s2 = 0
        s3 = 0
        for s in tmp:
            if s in [1, 10]:
                continue
            if 2 <= s <= 5:
                s1 = 1
            if 4 <= s <= 7:
                s3 = 1
            if 6 <= s <= 9:
                s2 = 1
        if s1 and s2 and s3:
            res -= 2
        elif s1 and s2 and not s3:
            res -= 1
        elif not s1 and not s2 and not s3:
            res -= 0
        else:
            res -= 1
        q.append((r, c))
    tmp = []
    while q:
        tmp.append(q.pop()[1])
    s1 = 0
    s2 = 0
    s3 = 0
    for s in tmp:
        if s in [1, 10]:
            continue
        if 2 <= s <= 5:
            s1 = 1
        if 4 <= s <= 7:
            s3 = 1
        if 6 <= s <= 9:
            s2 = 1
    if s1 and s2 and s3:
        res -= 2
    elif s1 and s2 and not s3:
        res -= 1
    elif not s1 and not s2 and not s3:
        res -= 0
    else:
        res -= 1
    return res


def maxNumberOfFamilies2(n, reservedSeats):
    d = {}
    res = n * 2
    for r, c in reservedSeats:
        if r not in d:
            d[r] = []
        d[r].append(c)
    for k in d:
        s1, s2, s3 = 0, 0, 0
        for s in d[k]:
            if s in [1, 10]:
                continue
            if 2 <= s <= 5:
                s1 = 1
            if 4 <= s <= 7:
                s3 = 1
            if 6 <= s <= 9:
                s2 = 1
        if s1 and s2 and s3:
            res -= 2
        elif s1 and s2 and not s3:
            res -= 1
        elif not s1 and not s2 and not s3:
            res -= 0
        else:
            res -= 1
    return res


class Solution(object):
    def getKth(self, lo, hi, k):
        res = []
        self.mem = {}
        for i in range(lo, hi + 1):
            l = self.compute(i, 0)
            res.append((l, i))
        return sorted(res)[k - 1][1]

    def compute(self, x, level):
        if x == 1:
            return level

        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        if x in self.mem:
            return self.mem[x]
        ans = self.compute(x, level + 1)
        return ans





if __name__ == '__main__':
    print(maxNumberOfFamilies2(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
    # s = Solution()
    # print(s.getKth(12, 15, 2))