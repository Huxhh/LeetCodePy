# coding=utf-8
# author huxh
# time 2020/4/30 12:25 AM


class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = self.com(n)
        if n == 1:
            return True
        return False

    def com(self, n):
        res = 0
        while n:
            tmp = n % 10
            n //= 10
            res += tmp * tmp
        return res