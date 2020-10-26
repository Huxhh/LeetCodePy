# coding=utf-8
# author huxh
# time 2020/8/2 12:38 AM


# 时间复杂度O(knlogk)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq

        dummy = ListNode(0)
        node = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(node, (lists[i].val, i))
                lists[i] = lists[i].next

        cur = dummy
        while node:
            top, idx = heapq.heappop(node)
            cur.next = ListNode(top)
            cur = cur.next

            if lists[idx]:
                heapq.heappush(node, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next



class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        n = len(lists)
        while n > 1:
            k = (n + 1) / 2
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
