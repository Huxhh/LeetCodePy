# coding=utf-8
# author huxh
# time 2020/8/2 11:57 PM


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            tmp = []
            l = []
            for i in range(len(q)):
                r = q.pop(0)
                if not r:
                    continue
                l.append(r.val)
                if r.left:
                    tmp.append(r.left)
                if r.right:
                    tmp.append(r.right)
            q = tmp
            res.append(l[:])
        return res

class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            l = []
            for i in range(len(q)):
                r = q.popleft()
                if not r:
                    continue
                l.append(r.val)
                if r.left:
                    l.append(r.left)
                if r.right:
                    l.append(r.right)
            res.append(l[:])
        return res
