# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    res = ListNode(0)
    tmp = res
    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        elif l1 is not None and l2 is None:
            tmp.next = l1
            break
        elif l1 is None and l2 is not None:
            tmp.next = l2
            break

    res = res.next
    return res


def mergeTwoLists2(l1, l2):
    res = tmp = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    tmp.next = l1 or l2
    return res.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    # print(mergeTwoLists(l1, l2))
    res = mergeTwoLists2(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next