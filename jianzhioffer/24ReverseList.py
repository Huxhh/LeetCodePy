# coding=utf-8
# author huxh
# time 2020/3/24 11:12 AM

# O(n) O(1)
def  reverseList(head):
    if not head:
        return head

    pre = None
    cur = head
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre
