# coding=utf-8
# author huxh
# time 2020/8/9 11:16 PM


class Solution:
    def strToInt(self, str: str) -> int:
        s = str
        s = s.strip(' ')
        if not s:
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        p, res = 0, 0
        while p < len(s) and s[p].isnumeric():
            res = res * 10 + int(s[p])
            p += 1

        return max(-(2**31), min(2**31-1, sign * res))
