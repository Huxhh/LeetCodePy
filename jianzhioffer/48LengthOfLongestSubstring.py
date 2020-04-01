# coding=utf-8
# author huxh
# time 2020/4/1 11:50 PM


def lengthOfLongestSubstring(s):
    if not s:
        return 0

    d = {}
    j = 0
    res = 0
    for i in range(len(s)):
        if s[i] in d:
            j = max(d[s[i]], j)
        res = max(res, i - j + 1)
        d[s[i]] = i + 1
    return res
