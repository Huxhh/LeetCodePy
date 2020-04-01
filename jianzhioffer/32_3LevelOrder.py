# coding=utf-8
# author huxh
# time 2020/3/27 3:50 PM


def levelOrder(root):
    if not root:
        return []

    res = []
    s1 = []
    s2 = []
    s1.append(root)
    i = 0
    while s1 or s2:
        if not i & 1:
            tmp = []
            while s1:
                r = s1.pop()
                tmp.append(r.val)
                if r.left:
                    s2.append(r.left)
                if r.right:
                    s2.append(r.right)
            res.append(tmp)
        else:
            tmp = []
            while s2:
                r = s2.pop()
                tmp.append(r.val)
                if r.right:
                    s1.append(r.right)
                if r.left:
                    s1.append(r.left)
            res.append(tmp)
        i += 1
    return res
