# coding=utf-8


"""
思路
首先设置一个哑结点用于指向头结点，然后两两进行交换，注意要保留一个pre节点作为交换中的两个节点的前一个节点
时间复杂度 O(n^2) 空间复杂度 O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = head
    pre = dummy
    while pre.next and pre.next.next:
        pre.next = current.next
        current.next = current.next.next
        pre.next.next = current
        pre = current
        current = current.next

    return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    head = swapPairs(l1)
    while head:
        print(head.val)
        head = head.next



