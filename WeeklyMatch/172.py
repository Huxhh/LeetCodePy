# coding=utf-8

def maximum69Number(num):
    array = [-1] * 4

    i = 0
    while num > 0:
        array[i] = num % 10
        num //= 10
        i += 1

    index = 0
    for k in range(4):
        index = k
        if array[k] == -1:
            break

    if array[index] == -1:
        index -= 1
    for j in range(index, -1, -1):
        if array[j] == 6:
            array[j] = 9
            break

    res = 0
    for j in range(index, -1, -1):
        res = res * 10 + array[j]
    return res


def printVertically(s):
    if not s:
        return []

    words = s.split(' ')
    max_len = 0
    for w in words:
        if len(w) > max_len:
            max_len = len(w)

    res = [""] * max_len
    for i in range(max_len):
        for word in words:
            if len(word) - 1 >= i:
                res[i] += word[i]
            else:
                res[i] += ' '

    for k in range(len(res)):
        res[k] = res[k].rstrip()
    return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def removeLeafNodes(self, root, target):
        if not root:
            return []
        self.deleteNode(root, target)

        if root.val == 0:
            return []

        self.dNode(root)
        return root


    def deleteNode(self, root, target):
        if root.left:
            self.deleteNode(root.left, target)
        if root.right:
            self.deleteNode(root.right, target)
        if not root.left and not root.right and root.val == target:
            root.val = 0

        elif root.val == target and not root.right and root.left:
            if root.left.val == 0:
                root.val = 0

        elif root.val == target and not root.left and root.right:
            if root.right.val == 0:
                root.val = 0

        elif root.val == target and root.left.val == 0 and root.right.val == 0:
            root.val = 0

        return

    def dNode(self, root):
        if root.left:
            if root.left.val == 0:
                root.left = None
            else:
                self.dNode(root.left)
        if root.right:
            if root.right.val == 0:
                root.right = None
            else:
                self.dNode(root.right)
        return

class Solution2(object):
    def removeLeafNodes(self, root, target):
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None

        return root


def minTaps(n, ranges):
    res = [-1] * (n + 1)
    for i in range(n + 1):
        for j in range(i - ranges[i], i + ranges[i]):
            if 0 <= j <= n:
                res[j] = 1
    if sum(res) != n + 1:
        return -1




if __name__ == '__main__':
    # print(maximum69Number(696))
    s = "AA BBB C DDDD EEEEE F"
    print(printVertically(s))