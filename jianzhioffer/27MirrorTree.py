# coding=utf-8
# author huxh
# time 2020/3/25 10:27 AM


def mirrorTree(root):
    if not root:
        return

    root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
    return root
