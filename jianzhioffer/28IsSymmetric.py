# coding=utf-8
# author huxh
# time 2020/3/25 10:34 AM


def isSymmetric(root):
    def back(a, b):
        if not a and not b:
            return True

        if not a or not b:
            return False

        if a.val == b.val:
            return back(a.left, b.right) and back(a.right, b.left)
        else:
            return False

    return back(root, root)


def isSymmetric2(root):
    if not root:
        return True

    q = []
    q.append(root.left)
    q.append(root.right)
    while q:
        a = q.pop(0)
        b = q.pop(0)
        if not a and not b:
            continue
        if not a or not b or a.val != b.val:
            return False
        q.append(a.left)
        q.append(b.right)
        q.append(a.right)
        q.append(b.left)
    return True

