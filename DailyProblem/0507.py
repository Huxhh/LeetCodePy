# coding=utf-8
# author huxh
# time 2020/5/7 10:08 AM


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.back(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def back(self, a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        if a.val != b.val:
            return False

        return self.back(a.right, b.right) and self.back(a.left, b.left)
