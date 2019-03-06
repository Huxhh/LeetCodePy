# coding=utf-8


"""
思路
首先找到所有字符串中长度最短的一个，将它用enumerate表示，即字符下标与字符一一对应
遍历其他字符串，每个字符与enumera中的字符比较，出现不同时返回下标得到结果
时间复杂度 O(m*n) 空间复杂度O(n)
"""


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
    for i, ss in enumerate(minlen):
        for other in strs:
            if other[i] != ss:
                return minlen[:i]
    return minlen


if __name__ == '__main__':
    print(longestCommonPrefix2(["flower","flow","flight"]))
    # strs = ["flower","flow","flight"]
    # print(list(enumerate(strs)))