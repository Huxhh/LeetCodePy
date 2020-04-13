# coding=utf-8
# author huxh
# time 2020/4/2 10:23 AM


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        vis = {}

        def dfs(head):
            if not head:
                return None
            if head in vis:
                return vis[head]

            newnode = Node(head.val)
            vis[head] = newnode
            newnode.next = dfs(head.next)
            newnode.random = dfs(head.random)
            return newnode

        return dfs(head)
