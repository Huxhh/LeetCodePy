# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = head
    length = 0
    while first is not None:
        first = first.next
        length += 1

    first = dummy
    length -= n
    while length > 0:
        length -= 1
        first = first.next

    first.next = first.next.next
    return dummy.next


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(0, n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next