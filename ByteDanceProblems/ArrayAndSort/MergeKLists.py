# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
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
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return newhead.next


def mergeKLists(self, lists):
    # 遍历链表，将所有链表的所有元素放到一个数组里面
    nodeList = []
    for i in range(len(lists)):
        currentNode = lists[i]
        # 遍历某个链表
        while (currentNode):
            nodeList.append(currentNode)
            currentNode = currentNode.next

    # 根据node的val对数组进行排序
    nodeList = sorted(nodeList, key=lambda x: x.val)

    # 对排序好的数组的元素，一个个地连接成新的链表（这里的tempHead是为了方便设置的头节点）
    tempHead = ListNode(0)
    currentNode = tempHead
    for i in range(len(nodeList)):
        currentNode.next = nodeList[i]
        currentNode = currentNode.next

    return tempHead.next
