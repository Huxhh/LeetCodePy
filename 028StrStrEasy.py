# coding=utf-8


"""
思路：
获取needle的长度，如果长度为0，即needle为空串，返回0
以needle的长度遍历haystack，出现相同时即返回下标
时间复杂度 O(n) 空间复杂度 O(1)
"""


def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    for i in range(0, len(haystack)):
        if haystack[i] == needle[0]:
            index = i
            flag = 1
            for j in range(0, len(needle)):
                if index >= len(haystack):
                    return -1
                if haystack[index] != needle[j]:
                    flag = 0
                    break
                index += 1
            if flag:
                return i
            else:
                continue
    return -1


def strStr2(haystack, needle):
    nlen = len(needle)
    if not nlen:
        return 0
    for i in range(nlen, len(haystack) + 1):
        if haystack[i - nlen: i] == needle:
            return i - nlen
    return -1


if __name__ == '__main__':
    haystack = "a"
    needle = "a"
    print(strStr2(haystack, needle))

