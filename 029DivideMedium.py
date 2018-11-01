# coding=utf-8


def divide(dividend, divisor):
    flag = (dividend > 0) == (divisor > 0)
    if dividend == 0:
        return 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    res = 0
    while dividend >= divisor:
        tmp, i = divisor, 1
        while dividend >= tmp:
            dividend -= tmp
            res += i
            tmp *= 2
            i *= 2

    if not flag:
        res = -res

    return min(max(res, -2147483648), 2147483647)


if __name__ == '__main__':
    dividend = 7
    divisor = -3
    print(divide(dividend, divisor))

