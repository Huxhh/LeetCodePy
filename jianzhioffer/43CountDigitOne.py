# coding=utf-8
# author huxh
# time 2020/3/31 11:58 AM

import math

def countDigitOne(n):

    def back(n):
        if n <= 9:
            return 1
        s = str(n)

        high = int(s[0])
        p = int(math.pow(10, len(s) - 1))
        last = n - high * p
        if high == 1:
            return back(p - 1) + last + 1 + back(last)
        else:
            return p + high * back(p - 1) + back(last)

    return back(n)
