# coding=utf-8


"""
思路
主要难度在进行溢出检查，检查分两部分，一部分是res>maxint/10时，加上tmp肯定溢出，还有一种是res=maxint/10时如果tmp>7
则发生溢出，另外由于python除法采用向下取整，因此将负数转化为正数来处理 时间复杂度O(log(x)) 空间复杂度O(1)
"""


def reverse(x):
    flag = 0
    if x < 0:
        x = -x
        flag = 1
    maxint = 2147483647
    res = 0
    while x > 0:
        tmp = x % 10
        if res > (maxint // 10):
            return 0
        elif res == (maxint // 10) and tmp > 7:
            return 0
        else:
            res = res * 10 + tmp
        x //= 10
    if flag:
        res = -res
    return res


if __name__ == '__main__':
    print(reverse(1463847412))
