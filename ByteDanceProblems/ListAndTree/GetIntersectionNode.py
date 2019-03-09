# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    alen = 0
    blen = 0
    a = headA
    b = headB
    while a:
        a = a.next
        alen += 1
    while b:
        b = b.next
        blen += 1

    if alen > blen:
        for i in range(alen - blen):
            headA = headA.next
    else:
        for i in range(blen - alen):
            headB = headB.next

    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    a = headA
    b = headB
    while a != b:
        if a:
            a = a.next
        else:
            a = headB
        if b:
            b = b.next
        else:
            b = headA

    return a
