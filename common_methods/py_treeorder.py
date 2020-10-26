# coding=utf-8
# author huxh
# time 2020/9/9 9:41 PM


def preorder(root):
    res = []

    def back(node):
        if not node:
            return

        res.append(node.val)
        back(node.left)
        back(node.right)
    back(root)
    return res

def preorder2(root):
    res = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left

        if stack:
            cur = stack.pop()
            cur = cur.right
    return res


def inorder(root):
    res = []

    def back(node):
        if not node:
            return

        back(node.left)
        res.append(node.val)
        back(node.right)

    back(root)
    return res

def inorder2(root):
    res = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left

        if stack:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


def postorder(root):
    res = []

    def back(node):
        if not node:
            return

        back(node.left)
        back(node.right)
        res.append(node.val)

    back(root)
    return res

def postorder2(root):
    res = []
    stack = []
    last = None
    cur = root
    while cur:
        stack.append(cur)
        cur = cur.left
    while stack:
        cur = stack.pop()
        if not cur.right or cur.right == last:
            res.append(cur.val)
            last = cur
        else:
            stack.append(cur)
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left
    return res

def postorder3(root):
    if root is None:
        return []

    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)

    return output[::-1]


def postorder4(root):
    if not root:
        return[]

    stack = []
    res = []
    last = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == last:
            res.append(root.val)
            last = root
            root = None
        else:
            stack.append(root)
            root = root.right
    return res
