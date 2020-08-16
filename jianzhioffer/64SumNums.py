# coding=utf-8
# author huxh
# time 2020/6/2 10:23 AM


class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res

