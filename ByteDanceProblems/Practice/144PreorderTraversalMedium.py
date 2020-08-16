# coding=utf-8
# author huxh
# time 2020/7/5 10:27 PM


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res
