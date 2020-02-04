# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        length = self.getLen(head)
        if length == 1:
            return head
        mov = k % length
        if mov == 0:
            return head
        tmp = head
        for _ in range(length - mov - 1):
            tmp = tmp.next
        newhead = tmp.next
        tmp.next = None
        tmp2 = newhead
        while tmp2.next:
            tmp2 = tmp2.next
        tmp2.next = head
        return newhead

    def getLen(self, head):
        lens = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            lens += 1

        return lens


def rotateRight(head, k):
    if not head:
        return head
    if not head.next:
        return head

    old_tail = head
    n = 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1

    old_tail.next = head
    newtail = head
    for i in range(n - k % n - 1):
        newtail = newtail.next

    newhead = newtail.next
    newtail.next = None
    return newhead


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)

    s = Solution()
    res = s.rotateRight(head, 0)
    while res:
        print(res.val)
        res = res.next
