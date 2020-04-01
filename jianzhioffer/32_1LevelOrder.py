# coding=utf-8
# author huxh
# time 2020/3/27 3:36 PM


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(N) O(N)
def levelOrder(root):
    res = []
    if not root:
        return res

    q = []
    q.append(root)
    while q:
        r = q.pop(0)
        res.append(r.val)
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
    return res
