# coding=utf-8
# author huxh
# time 2020/7/5 9:46 PM


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = pre

        while tail:
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            after_next = tail.next
            start = pre.next
            tail.next = None
            pre.next = self.reverse(start)
            start.next = after_next
            pre = tail = start

        return dummy.next

    def reverse(self, head):
        pre = None
        cur = head
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
