# coding=utf-8
# author huxh
# time 2020/8/17 12:47 AM


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        n = len(path)
        s = []
        pos = 0
        while pos < n:
            while pos < n and path[pos] == '/':
                pos += 1
            tmps = ''
            while pos < n and path[pos] != '/':
                tmps += path[pos]
                pos += 1

            if tmps == '..':
                if s:
                    s.pop(-1)
            elif tmps != '' and tmps != '.':
                s.append(tmps)

        if not s:
            return '/'
        res = ''
        while s:
            res = '/' + s.pop(-1) + res

        return res
