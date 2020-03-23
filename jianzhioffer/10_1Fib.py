# coding=utf-8
# author huxh
# time 2020/3/20 11:52 AM


def fib(n):
    d = {}
    def back(n):
        if n in d:
            return d[n]
        if n == 0:
            return 0
        if n == 1:
            return 1

        res = back(n - 1) + back(n - 2)
        d[n] = res
        return res

    return back(n) % int(1e9 + 7)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a % int(1e9 + 7)

