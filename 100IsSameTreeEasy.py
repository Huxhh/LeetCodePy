# coding=utf-8

"""
思路
方法一：递归，比较树的每个左子树与右子树，得到结果
方法二：使用栈结构，先将根节点入栈，比较之后将左右节点压入栈中进行比较
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False


def isSameTree2(p, q):
    stack = [(p, q)]
    while stack:
        n1, n2 = stack.pop()
        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        elif not n1 and not n2:
            continue
        else:
            return False
    return True



if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t2 = TreeNode(1)
    t2.right = TreeNode(2)
    print(isSameTree2(t1, t2))