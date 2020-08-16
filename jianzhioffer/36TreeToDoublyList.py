# coding=utf-8
# author huxh
# time 2020/7/20 11:48 PM


# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.pre = None
        self.head = None

        def inorder(r):
            if r:
                inorder(r.left)

                if not self.pre:
                    self.head = r
                else:
                    self.pre.right, r.left = r, self.pre
                self.pre = r
                inorder(r.right)

        inorder(root)
        self.pre.right, self.head.left = self.head, self.pre
        return self.head

