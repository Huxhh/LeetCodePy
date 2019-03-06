# coding=utf-8

def longestCommonPrefix(strs):
    if not strs:
        return ""

    minlen = min(strs, key=len)

    for i, s in enumerate(minlen):
        for others in strs:
            if others[i] != s:
                return minlen[:i]

    return minlen
