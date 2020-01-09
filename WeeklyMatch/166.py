# coding=utf-8


def subtractProductAndSum(n):
    mulres = 1
    sumres = 0

    while n:
        mulres *= (n % 10)
        sumres += (n % 10)
        n //= 10

    return mulres - sumres


def groupThePeople(groupSizes):
    if not groupSizes:
        return []

    dic = {}
    res = []
    for i in range(len(groupSizes)):
        if groupSizes[i] not in dic:
            dic[groupSizes[i]] = []
        dic[groupSizes[i]].append(i)
        if len(dic[groupSizes[i]]) == groupSizes[i]:
            res.append(dic[groupSizes[i]])
            dic.pop(groupSizes[i])

    return res


def smallestDivisor(nums, threshold):
    if not nums:
        return None

    l, r, ans = 1, max(nums), -1
    while l <= r:
        mid = (l + r) // 2
        total = sum([(x - 1) // mid + 1 for x in nums])
        if total > threshold:
            l = mid + 1
        else:
            ans = mid
            r = mid - 1

    return ans


import queue
class Solution(object):
    def encode(self, mat, m, n):
        res = 0
        for i in range(m):
            for j in range(n):
                res = res * 2 + mat[i][j]
        return res

    def decode(self, x, m, n):
        mat = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mat[i][j] = x & 1
                x >>= 1
        return mat

    def convert(self, mat, m, n, i, j):
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]:
            i0 = i + di
            j0 = j + dj
            if 0 <= i0 < m and 0 <= j0 < n:
                mat[i0][j0] ^= 1

    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        x_start, step = self.encode(mat, m, n), 0
        if x_start == 0:
            return step

        visited = {x_start}
        q = queue.Queue()
        q.put_nowait(x_start)

        while not q.empty():
            step += 1
            k = q.qsize()
            for _ in range(k):
                status = self.decode(q.get_nowait(), m, n)
                for i in range(m):
                    for j in range(n):
                        self.convert(status, m, n, i, j)
                        x_cur = self.encode(status, m, n)
                        if x_cur == 0:
                            return step
                        if x_cur not in visited:
                            visited.add(x_cur)
                            q.put_nowait(x_cur)
                        self.convert(status, m, n, i, j)

        return -1


class Solution2:
    def __init__(self):
        self.ans = 10**9

    def convert(self, mat, m, n, i, j):
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            i0 = i + di
            j0 = j + dj
            if 0 <= i0 < m and 0 <= j0 < n:
                mat[i0][j0] ^= 1

    def dfs(self, mat, m, n, pos, step):
        if pos == m * n:
            if all(mat[i][j] == 0 for i in range(m) for j in range(n)):
                self.ans = min(self.ans, step)
            return

        x, y = pos // n, pos % n
        self.dfs(mat, m, n, pos + 1, step)

        self.convert(mat, m, n, x, y)
        self.dfs(mat, m, n, pos + 1, step + 1)
        self.convert(mat, m, n, x, y)

    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        self.dfs(mat, m, n, 0, 0)
        return self.ans if self.ans != 10 ** 9 else -1


if __name__ == '__main__':
    # print(subtractProductAndSum(4421))
    # groupSizes = [2,1,3,3,3,2]
    # print(groupThePeople(groupSizes))
    nums = [1,2,5,9]
    threshold = 6
    print(smallestDivisor(nums, threshold))