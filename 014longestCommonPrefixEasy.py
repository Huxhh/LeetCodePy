# coding=utf-8


def longestCommonPrefix(strs):
    res = ""
    if len(strs) == 0:
        return res
    flag = 1
    i = 0
    for s in strs:
        if len(s) == 0:
            return res
    while flag:
        if i >= len(strs[0]):
            break
        tmps = strs[0][i]
        for s in strs:
            if i >= len(s):
                flag = 0
                break

            if s[i] != tmps:
                flag = 0

        i += 1
        if flag:
            res += tmps
        else:
            break

    return res


def longestCommonPrefix2(strs):
    if not strs:
        return ""
    minlen = min(strs, key=len)
    print(minlen)
    print(list(enumerate(minlen)))
    for i, ss in enumerate(minlen):
        for other in strs:
            if other[i] != ss:
                return minlen[:i]
    return minlen


if __name__ == '__main__':
    print(longestCommonPrefix2(["flower","flow","flight"]))
    # strs = ["flower","flow","flight"]
    # print(list(enumerate(strs)))