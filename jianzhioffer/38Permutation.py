# coding=utf-8
# author huxh
# time 2020/3/28 11:26 AM


def permutation(s):
    if not s:
        return []
    res = set()
    vis = [0] * len(s)

    def back(st):
        if len(st) == len(s):
            res.add(st)
            return

        for i in range(len(s)):
            if not vis[i]:
                vis[i] = 1
                back(st + s[i])
                vis[i] = 0
    back('')
    return list(res)


def permutation2(s):
    if not s:
        return []
    res = []

    def back(st, cs):
        if len(st) == len(s):
            res.append(st)
            return
        vis = {}
        for i in range(len(cs)):
            # if i and cs[0] == cs[i]:
            #     continue
            if cs[i] in vis:
                continue
            vis[cs[i]] = 1
            cs[0], cs[i] = cs[i], cs[0]
            back(st + cs[0], cs[1:])
            cs[0], cs[i] = cs[i], cs[0]
    s = list(s)
    back('', s)
    return res


def permutation3(s):
    if not s:
        return []

    s = sorted(list(s))
    res = []

    def back(st, tmp):
        if not st:
            res.append(tmp)
            return
        for i in range(len(st)):
            if i and st[i] == st[i - 1]:
                continue
            back(st[:i] + st[i + 1:], tmp + st[i])
    back(s, '')
    return res



if __name__ == '__main__':
    print(permutation3("aac"))
