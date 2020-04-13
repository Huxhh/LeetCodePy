# coding=utf-8
# author huxh
# time 2020/4/3 1:20 PM


def isBalanced(root):
    ans = [True]

    def back(r):
        if not r:
            return 0

        left = back(r.left)
        right = back(r.right)
        if abs(left - right) > 1:
            ans[0] = False
        return max(left, right) + 1
    back(root)

    return ans[0]


def isBalanced2(root):

    def back(r):
        if not r:
            return 0
        l = back(r.left)
        if l == -1:
            return -1
        r = back(r.right)
        if r == -1:
            return -1
        return max(l, r) + 1 if abs(l - r) <= 1 else -1
    return back(root) != -1
