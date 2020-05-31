# coding=utf-8

class Solution(object):
    def reverseList(self, head):
        pre = None
        curr = head
        while curr:
            curr.next, pre, curr = pre, curr, curr.next
        return pre