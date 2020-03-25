# coding=utf-8
# author huxh
# time 2020/3/24 11:05 AM

# O(n) O(1)
def getKthFromEnd(head, k):
    if not head:
        return None

    p1 = head
    p2 = head
    while k:
        p1 = p1.next
        k -= 1

    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2