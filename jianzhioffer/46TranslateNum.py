# coding=utf-8
# author huxh
# time 2020/4/1 11:26 PM


def translateNum(num):
    if num <= 9:
        return 1

    tail = num % 100
    if tail <= 9 or tail >= 26:
        return translateNum(num // 10)
    else:
        return translateNum(num // 10) + translateNum(num // 100)
