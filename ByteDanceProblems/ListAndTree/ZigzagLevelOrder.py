# coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzagLevelOrder(root):
    if not root:
        return []

    stacks = [[], []]
    current = 0
    nexts = 1
    res = []
    tmp = []

    stacks[current].append(root)
    while stacks[0] or stacks[1]:
        node = stacks[current].pop(-1)
        tmp.append(node.val)

        if current == 0:
            if node.left:
                stacks[nexts].append(node.left)
            if node.right:
                stacks[nexts].append(node.right)
        else:
            if node.right:
                stacks[nexts].append(node.right)
            if node.left:
                stacks[nexts].append(node.left)

        if not stacks[current]:
            current = 1 - current
            nexts = 1 - nexts
            res.append(tmp)
            tmp = []
    return res
