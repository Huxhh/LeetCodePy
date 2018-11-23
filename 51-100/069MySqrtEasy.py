# coding=utf-8

"""
思路：
方法一：暴力，会超时
方法二：二分查找
方法三：牛顿法，详见https://en.wikipedia.org/wiki/Integer_square_root
"""

def mySqrt(x):
    i = 1
    while i * i <= x:
        i += 1
    return i - 1


def mySqrt2(x):
    if x < 2:
        return x
    l = 0
    r = x // 2
    ans = 1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid > x:
            r = mid - 1
        elif mid * mid < x:
            l = mid + 1
            ans = mid
        else:
            return mid
    return ans


def mySqrt3(x):
    if x < 2:
        return x
    ans = x // 2
    while ans > x / ans:
        ans = (ans + x / ans) // 2
    return int(ans)


if __name__ == '__main__':
    print(mySqrt3(10))