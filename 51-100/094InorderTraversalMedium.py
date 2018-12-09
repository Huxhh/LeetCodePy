# coding=utf-8


"""
思路：
方法一：递归中序遍历
    时间复杂度 O(n) 空间复杂度 最坏 O(n) 平均 O(logn)
方法二：使用栈迭代计算
    时间复杂度 O(n) 空间复杂度 O(n)
方法三：见leetcode解答，即左子树不为空时，将右子树变成左子树中最大值的右子树
    https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def inorderTraversal(self, root):
        res = []
        if not root:
            return res
        self.inOrder(root, res)
        return res

    def inOrder(self, node, res):
        if node.left:
            self.inOrder(node.left, res)
        res.append(node.val)
        if node.right:
            self.inOrder(node.right, res)
        return


def inorderTraversal(root):
    res = []
    if not root:
        return res
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    # print(s.inorderTraversal(root))
    print(inorderTraversal(root))