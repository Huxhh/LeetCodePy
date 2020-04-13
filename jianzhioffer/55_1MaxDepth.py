# coding=utf-8
# author huxh
# time 2020/4/3 1:06 PM


def maxDepth(root):
    if not root:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def maxDepth2(root):
    if not root:
        return 0

    q = []
    res = 0
    q.append(root)
    while q:
        tmp = []
        for n in q:
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
        q = tmp
        res += 1
    return res