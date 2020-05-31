# coding=utf-8
# author huxh
# time 2020/5/23 10:34 AM


def minWindow(s, t):
    ori = {}
    cnt = {}

    def check():
        for c in ori:
            if c not in cnt or cnt[c] < ori[c]:
                return False
        return True

    for c in t:
        if c not in ori:
            ori[c] = 0
        ori[c] += 1

    l = 0
    r = -1
    ansL = -1
    ansR = -1
    ansLen = 1e9
    while r < len(s):
        r += 1
        if r < len(s) and s[r] in ori:
            if s[r] not in cnt:
                cnt[s[r]] = 0
            cnt[s[r]] += 1
        while check() and l <= r:
            if r - l + 1 < ansLen:
                ansLen = r - l + 1
                ansL = l
                ansR = l + ansLen

            if s[l] in ori:
                cnt[s[l]] -= 1
            l += 1
    return '' if ansL == -1 else s[ansL:ansR]


