# coding=utf-8
# author huxh
# time 2020/8/3 12:03 AM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                index = i
                break

        root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

