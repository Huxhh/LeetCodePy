# -*- coding: utf-8 -*-


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