# coding=utf-8
# author huxh
# time 2020/4/14 10:32 AM


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        head = ListNode(0)
        cur = head
        carry = 0
        while s1 and s2:
            tmp = s1.pop() + s2.pop() + carry
            cur.next = ListNode(tmp % 10)
            carry = tmp // 10
            cur = cur.next

        if s1:
            while s1:
                tmp = s1.pop() + carry
                cur.next = ListNode(tmp % 10)
                carry = tmp // 10
                cur = cur.next
        if s2:
            while s2:
                tmp = s2.pop() + carry
                cur.next = ListNode(tmp % 10)
                carry = tmp // 10
                cur = cur.next
        if carry:
            cur.next = ListNode(carry)

        s = []
        head = head.next
        while head:
            s.append(head.val)
            head = head.next
        newhead = ListNode(0)
        cur = newhead
        while s:
            newhead.next = ListNode(s.pop())
            newhead = newhead.next
        return cur.next


def addTwoNumbers(l1, l2):
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    ans = None
    carry = 0
    while s1 or s2 or carry != 0:
        a = 0 if not s1 else s1.pop()
        b = 0 if not s2 else s2.pop()
        cur = a + b + carry
        carry = cur // 10
        cur %= 10
        curnode = ListNode(cur)
        curnode.next = ans
        ans = curnode
    return ans

