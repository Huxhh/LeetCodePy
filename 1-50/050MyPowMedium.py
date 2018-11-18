# coding=utf-8


def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1 / x
    if n % 2 == 0:
        return myPow(x * x, n // 2)
    else:
        return x * myPow(x * x, n // 2)


def myPow2(x, n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1 / x
    res = 1.0
    while n:
        if n % 2 == 1:
            res *= x
        x *= x
        n //= 2
    return res


if __name__ == '__main__':
    print(myPow2(2.0000, -2))