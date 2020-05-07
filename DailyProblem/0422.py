# coding=utf-8
# author huxh
# time 2020/4/22 11:03 AM


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rightSideView(root):
    if not root:
        return []
    q = []
    q.append(root)
    level = []
    while q:
        tmp = []
        for i in range(len(q)):
            r = q.pop(0)
            tmp.append(r.val)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        level.append(tmp)

    res = []
    for l in level:
        res.append(l[-1])
    return res


from collections import deque

def rightSideView2(root):
    d = {}
    max_depth = -1
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if node:
            max_depth = max(depth, max_depth)
            d[max_depth] = node.val

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    return [d[i] for i in range(max_depth + 1)]


def rightSideView3(root):
    d = {}
    max_depth = -1
    stack = [(root, 0)]

    while stack:
        node, depth = stack.pop()

        if node:
            max_depth = max(depth, max_depth)
            d[depth] = node.val

            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return [d[i] for i in range(max_depth + 1)]
