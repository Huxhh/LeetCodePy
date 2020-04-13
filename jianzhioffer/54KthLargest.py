# coding=utf-8
# author huxh
# time 2020/4/3 12:09 PM


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthLargest(root, k):
    res = []

    def inorder(r, t):
        if not r:
            return t

        t = inorder(r.right, t)
        t += 1
        if t == k:
            res.append(r)
        if t < k:
            t = inorder(r.left, t)
        return t

    inorder(root, 0)
    return res[0].val


class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.res = 0
        self.k = k

        def dfs(root):
            if not root:
                return

            dfs(root.right)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            if self.k > 0:
                dfs(root.left)

        dfs(root)
        return self.ans