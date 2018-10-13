# coding=utf-8


"""
思路
方法一：原问题可以转化为删除链表第 L-n+1个节点，L为链表长度，因此可以遍历两边，
    第一遍遍历先获取链表的长度，第二次遍历找到第L-n+1个节点并删除
方法二：可以简化为只进行一次遍历，准备两个指针，首先把第一个指针移动n+1步，然后再同时移动
    两个指针，目的是为了可以让两个指针之间始终有n个节点，这样第一个指针移动到尾部后，将
    第二个指针的下一个节点删除即可
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = head
    length = 0
    while first is not None:
        first = first.next
        length += 1

    first = dummy
    length -= n
    while length > 0:
        length -= 1
        first = first.next

    first.next = first.next.next
    return dummy.next


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for i in range(0, n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next