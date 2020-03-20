# coding=utf-8


def replaceSpace(s):
    return s.replace(' ', '%20')


def replaceSpace(s):
    res = ''
    for c in s:
        if c == ' ':
            res += '%20'
        else:
            res += c
    return res
