# coding=utf-8
# author huxh
# time 2020/3/22 10:30 AM


def createTargetArray(nums, index):
    target = []

    for n, i in zip(nums, index):
        target = target[:i] + [n] + target[i:]

    return target

import math
class Solution(object):

    def sumFourDivisors(self, nums):
        res = 0
        for n in nums:
            res += self.getsum(n)
        return res

    def getsum(self, x):
        cnt = 1
        tmp = 0
        i = 2
        while i < math.sqrt(x):
            if x % i == 0:
                cnt += 1
                tmp = i + (x // i)
                if cnt > 2:
                    break
            i += 1
        if cnt == 2:
            return 1 + x + tmp
        return 0


def sumFourDivisors(nums):
    res = 0
    for n in nums:
        j = 0
        k = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                j += 1
                k += i
                if i * i < n:
                    j += 1
                    k += (n // i)
                i += 1
        if j == 4:
            res += k
    return res


def hasValidPath(grid):
    d = [{1:(0, 1, 1), 3:(0, -1, 3)},
         {2:(1, 0, 2), 4:(-1, 0, 4)},
         {1:(1, 0, 2), 4:(0, -1, 3)},
         {4:(0, 1, 1), 3:(1, 0, 2)},
         {1:(-1, 0, 4), 2:(0, -1, 3)},
         {2:(0, 1, 1), 3:(-1, 0, 4)}]

    out = d[grid[0][0] - 1].keys()
    for bo in out:
        i, j = 0, 0
        o = bo
        while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if o not in d[grid[i][j] - 1]:
                break

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True

            di, dj, newout = d[grid[i][j] - 1][o]
            i += di
            j += dj
            o = newout

    return False



if __name__ == '__main__':
    # print(createTargetArray([1], [0]))
    # s = Solution()
    # print(s.sumFourDivisors([1,2,3,4,5,6,7,8,9,10]))
    print(hasValidPath([[1,2,1],[1,2,1]]))