# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    current = head
    pre = dummy
    while current:
        while current.next and current.val == current.next.val:
            current = current.next
        if pre.next == current:
            pre = pre.next
        else:
            pre.next = current.next

        current = current.next

    return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    s = deleteDuplicates(head)
    while s:
        print(s.val)
        s = s.next