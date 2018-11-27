# coding=utf-8


"""
思路：
首先设置一个哑结点指向头结点，设置当前节点current指向head，前一个节点pre指向哑结点，
当当前节点current不为空时，开始循环，获取当前节点的下一个节点，如果存在且与当前节点值
相同，则当前节点指针后移，遇到不相同时，如果前置节点的下一个节点还是当前节点即表示当前节点
没有移动，则将前置节点移动至当前节点，否则，表示已经移动，那么当前节点的值也是重复的，
前置节点就跳过当前节点指向下一节点，然后当前节点在向后移动
循环结束后返回哑结点的下一个节点
"""


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