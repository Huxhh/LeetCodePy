# coding=utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        end = dummy

        while end:
            for i in range(k):
                if not end:
                    break
                end = end.next
            if not end:
                break
            start = pre.next
            after = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = after

            pre = end = start
        return dummy.next

    def reverse(self, head):
        pre = None
        curr = head
        while curr:
            curr.next, pre, curr = pre, curr, curr.next
        return pre

