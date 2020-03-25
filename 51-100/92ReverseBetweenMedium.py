# coding=utf-8
# author huxh
# time 2020/3/24 4:11 PM


def reverseBetween(head, m, n):
    if not head:
        return head

    pre, cur = None, head
    while m > 1:
        pre = cur
        cur = cur.next
        m -= 1
        n -= 1

    before = pre
    tail = cur
    while n:
        cur.next, pre, cur = pre, cur, cur.next
        n -= 1

    if before:
        before.next = pre
    else:
        head = pre
    tail.next = cur
    return head
