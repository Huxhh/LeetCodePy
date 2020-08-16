# coding=utf-8
# author huxh
# time 2020/8/2 12:34 AM

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return lists
        n = len(lists)
        while n > 1:
            k = (n + 1) // 2
            for i in range(0, n // 2):
                lists[i] = self.mergeTwoList(lists[i], lists[i + k])
            n = k
        return lists[0]

    def mergeTwoList(self, l1, l2):
        newhead = ListNode(0)
        cur = newhead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return newhead.next
