# coding=utf-8
# author huxh
# time 2020/5/19 10:29 AM


def validPalindrome(s):
    def check(l, h):
        while l < h:
            if s[l] == s[h]:
                l += 1
                h -= 1
            else:
                return False
        return True

    l = 0
    h = len(s) - 1
    while l < h:
        if s[l] == s[h]:
            l += 1
            h -= 1
        else:
            return check(l + 1, h) or check(l, h - 1)
    return True
