# coding=utf-8


"""
思路
本题思路是初等数学，即从最低位开始相加，有进位时保留，下一位相加时加上进位，
值得注意的是，在开始的地方使用哑结点简化代码，否则需要编写额外代码
时间复杂度 O(max(m, n)) 空间复杂度 O(max(m, n))
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    res = ListNode(0)
    current = res
    p = l1
    q = l2
    carry = 0
    while p or q:
        x = 0
        y = 0
        if p is not None:
            x = p.val
        if q is not None:
            y = q.val
        summary = x + y + carry
        carry = summary // 10
        current.next = ListNode(summary % 10)
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next
        current = current.next

    if carry:
        current.next = ListNode(carry)

    return res.next


if __name__ == '__main__':
    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    res = addTwoNumbers(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next