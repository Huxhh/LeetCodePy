# coding=utf-8
# author huxh
# time 2020/4/2 10:51 AM


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    p1 = headA
    p2 = headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1