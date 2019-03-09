# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        d = {}
        self.build(root, d)
        p1 = d[p]
        q1 = d[q]
        while p1 != q1:
            p1 = d[p1]
            q1 = d[q1]
        return p1

    def build(self, root, d):
        if not root:
            return
        if root.left:
            d[root.left] = root
        if root.right:
            d[root.right] = root

        self.build(root.left, d)
        self.build(root.right, d)


def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    if left:
        return left
    else:
        return right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    p = root.left
    q = root.right
    print(s.lowestCommonAncestor(root, p, q).val)