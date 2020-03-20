# coding=utf-8


def sortString(s):
    if not s:
        return ''

    res = ''
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1

    keys = sorted(d.keys())
    rkeys = sorted(d.keys(), reverse=True)

    while len(res) < len(s):
        for w in keys:
            if d[w] > 0:
                res += w
                d[w] -= 1

        for w in rkeys:
            if d[w] > 0:
                res += w
                d[w] -= 1

    return res


def findTheLongestSubstring(s):
    if not s:
        return 0

    d = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
    pos = [-1] * (1 << 5)
    cur = 0
    res = 0
    for i in range(len(s)):
        if s[i] in d:
            cur ^= (1 << d[s[i]])

        if pos[cur] == -1:
            pos[cur] = i + 1
        else:
            res = max(res, i + 1 - pos[cur])
    return res




class Solution(object):
    def longestZigZag(self, root):
        if not root:
            return 0

        return max(self.findZ(root.left, 0, 1), self.findZ(root.right, 0, 2))

    def findZ(self, root, level, d):
        if not root:
            return level

        if d == 1:
            if not root.right:
                return max(level + 1, self.findZ(root.left, 0, 1))
            else:
                return max(self.findZ(root.right, level + 1, 2), self.findZ(root.left, 0, 1))
        else:
            if not root.left:
                return max(level + 1, self.findZ(root.right, 0, 2))
            else:
                return max(self.findZ(root.left, level + 1, 1), self.findZ(root.right, 0, 2))


if __name__ == '__main__':
    print(sortString('spo'))
