# coding=utf-8
# author huxh
# time 2020/5/8 11:19 AM


def isUnique(astr):
    mark = 0
    for s in astr:
        index = ord(s) - ord('a')
        if mark & 1 << index:
            return False
        else:
            mark |= 1 << index
    return True
