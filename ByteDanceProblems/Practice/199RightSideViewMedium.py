# coding=utf-8
# author huxh
# time 2020/7/4 10:09 PM


def rightSideView(root):
    stack = [(root, 0)]
    res = {}
    max_depth = -1

    while stack:
        node, depth = stack.pop()
        max_depth = max(depth, max_depth)

        if node:
            res[depth] = node.val

            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

    return [res[i] for i in range(max_depth + 1)]
