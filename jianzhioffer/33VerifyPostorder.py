# coding=utf-8
# author huxh
# time 2020/3/27 4:27 PM


# O(n^2) O(n)
def verifyPostorder(postorder):
    def back(i, j):
        if i >= j:
            return True
        l = i
        while postorder[l] < postorder[j]:
            l += 1
        m = l
        while postorder[l] > postorder[j]:
            l += 1
        return l == j and back(i, m - 1) and back(m, j - 1)
    return back(0, len(postorder) - 1)


# O(N) O(N) ****
def verifyPostorder2(postorder):
    stack, root = [], float("+inf")
    for i in range(len(postorder) - 1, -1, -1):
        if postorder[i] > root: return False
        while stack and postorder[i] < stack[-1]:
            root = stack.pop()
        stack.append(postorder[i])
    return True

