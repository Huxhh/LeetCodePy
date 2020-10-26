# coding=utf-8
# author huxh
# time 2020/9/14 11:01 AM


def quick_power(base, exponent):
    res = 1
    while exponent:
        if exponent & 1:
            res *= base
        base *= base
        exponent >>= 2

    return res
