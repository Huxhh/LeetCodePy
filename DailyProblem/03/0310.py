# coding=utf-8

class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        mem = {}
        def getd(root, level):
            if not root:
                return level - 1

            if root in mem:
                return mem[root]

            res =  max(getd(root.left, level + 1), getd(root.right, level + 1))
            mem[root] = res
            return res

        q = []
        q.append(root)
        maxs = 0
        while q:
            r = q.pop(0)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
            maxs = max(maxs, getd(r.left, 1) + getd(r.right, 1))
        return maxs


class Solution2(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        self.ans = 0
        def getd(r):
            if not r:
                return 0

            L = getd(r.left)
            R = getd(r.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1

        getd(root)
        return self.ans