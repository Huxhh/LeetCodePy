# coding=utf-8

def simplifyPath(path):
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


if __name__ == '__main__':
    path = '/../'
    print(simplifyPath(path))


