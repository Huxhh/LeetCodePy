# coding=utf-8
# author huxh
# time 2020/3/19 10:21 PM


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(N) O(N)
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
                root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
                break
        return root


# O(N) O(N)   *****
def buildTree2(preorder, inorder):
    if not preorder or not inorder:
        return

    root = TreeNode(preorder[0])
    s = [root]
    inorderindex = 0
    for i in range(1, len(preorder)):
        if s[-1].val != inorder[inorderindex]:
            s[-1].left = TreeNode(preorder[i])
            s.append(s[-1].left)
        else:
            while s and s[-1].val == inorder[inorderindex]:
                node = s.pop()
                inorderindex += 1
            node.right = TreeNode(preorder[i])
            s.append(node.right)
    return root