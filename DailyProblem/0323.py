# coding=utf-8
# author huxh
# time 2020/3/23 9:35 AM


def middleNode(head):
    p1 = head
    p2 = head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    return p1