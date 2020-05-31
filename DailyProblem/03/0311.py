# coding=utf-8

def canThreePartsEqualSum(A):
    s = sum(A)
    if s % 3 != 0:
        return False

    n = len(A)
    target = s // 3
    c = 0
    index = 0
    for i in range(n):
        c += A[i]
        index = i
        if c == target:
            break
    if c != target:
        return False
    r = index + 1
    for j in range(r, n - 1):
        c += A[j]
        if c == target * 2:
            break
    if c == target * 2:
        return True
    return False
