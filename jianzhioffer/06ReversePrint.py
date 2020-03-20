# coding=utf-8
# author huxh
# time 2020/3/19 10:07 PM


# 时间O(N) 空间O(N)
def reversePrint(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res[::-1]

# O(N) O(N)  **
def reversePrint2(head):
    res = []
    def back(node):
        if not node:
            return

        back(node.next)
        res.append(node.val)
    back(head)
    return res

# O(N) O(N) **
def reversePrint3(head):
    res = []
    st = []
    while head:
        st.append(head)
        head = head.next
    while st:
        res.append(st.pop().val)
    return res

# O(N) O(1)
def reversePrint4(head):
    cur = head
    pre = None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next

    res = []
    while pre:
        res.append(pre.val)
        pre = pre.next
    return res