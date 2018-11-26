# coding=utf-8

"""
思路
方法一：当前节点与前一个节点的value比较，相等则跳过该节点
    时间复杂度 O(n) 空间复杂度 O(1)
方法二：见leetcode官方题解
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if not head or not head.next:
        return head
    tmp = head
    current = head
    while current:
        if current.val == tmp.val:
            current = current.next
        else:
            tmp.next = current
            tmp = current
            current = current.next
    tmp.next = current

    return head


def deleteDuplicates2(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head = deleteDuplicates2(head)
    s = head
    while s:
        print(s.val)
        s = s.next