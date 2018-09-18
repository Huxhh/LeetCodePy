# -*- coding: utf-8 -*-


"""
思路
方法1：将数字转换为字符串，判断首尾是否相等，依次循环，但需要额外空间存储字符串 时间复杂度O(n) 空间复杂度O(n)
方法2：反转一半数字，用%10取得最后位，再用/10（python中精确除法是/，取整是//）消去最后位，再将取出的
        最后位数字*10加上倒数第二位数字，直到原始数字小于反转数字 时间复杂度O(log10(n)) 空间复杂度O(1)
"""


def isPalindrome(x):
    if x < 0:
        return False
    s = str(x)
    lens = len(s)
    i, j = 0, lens - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


def isPalindrome2(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    ret = 0
    while x > ret:
        ret = ret * 10 + x % 10
        x //= 10

    return x == ret or x == ret // 10


if __name__ == '__main__':
    print(isPalindrome2(12321))