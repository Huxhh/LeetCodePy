# coding=utf-8
# author huxh
# time 2020/4/13 3:32 PM


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
