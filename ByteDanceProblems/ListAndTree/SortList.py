# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(head):
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    while cur.next:
        if cur.val <= cur.next.val:
            cur = cur.next
        else:
            tmp = cur.next
            cur.next = tmp.next
            p = dummy
            while p.next and p.next.val < tmp.val:
                p = p.next
            tmp.next = p.next
            p.next = tmp
    return dummy.next
