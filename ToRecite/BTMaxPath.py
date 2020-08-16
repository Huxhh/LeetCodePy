# coding=utf-8
# author huxh
# time 2020/8/3 12:43 AM


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def maxGain(node):
            if not node:
                return 0

            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            newSum = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, newSum)

            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
