# coding=utf-8
# author huxh
# time 2020/3/23 4:00 PM

# O(n) O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(head, val):
    if not head:
        return head

    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next:
        if p.next.val == val:
            break
        p = p.next

    p.next = p.next.next
    return dummy.next