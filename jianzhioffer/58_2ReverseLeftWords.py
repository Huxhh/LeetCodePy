# coding=utf-8
# author huxh
# time 2020/4/6 3:23 PM


def reverseLeftWords(s, n):
    return s[n:] + s[:n]


def reverseLeftWords2(s, n):
    if n > len(s) or not s:
        return ''
    s = list(s)

    def reverse(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    length = len(s) - 1
    reverse(0, n - 1)
    reverse(n, length)
    reverse(0, length)
    return ''.join(s)

