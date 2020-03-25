# coding=utf-8
# author huxh
# time 2020/3/25 10:13 AM


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# O(M+N) O(1)
def mergeTwoLists1(l1, l2):
    dummy = ListNode(0)
    p = dummy
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next

    p.next = l1 or l2
    return dummy.next


def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        node = l1
        node.next = mergeTwoLists(l1.next, l2)
    else:
        node = l2
        node.next = mergeTwoLists(l1, l2.next)
    return node
