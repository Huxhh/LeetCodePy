# coding=utf-8

"""
思路
思路比较常规，注意第二种方法的技巧即可
"""

def addBinary(a, b):
    n = len(a)
    m = len(b)
    if n < m:
        a, b, m, n = b, a, n, m

    l = []
    for x in a:
        l.append(x)
    for i in range(n - 1, n - m - 1, -1):
        l[i] = str(int(a[i]) + int(b[i - n + m]))

    c = 0
    for i in range(n - 1, -1, -1):
        tmp = int(l[i]) + c
        l[i] = str((int(l[i]) + c) % 2)
        c = tmp // 2

    ext = ""
    while c > 0:
        ext = str(c % 2) + ext
        c //= 2

    return ext + ''.join(l)


def addBinary2(a, b):
    m = len(a) - 1
    n = len(b) - 1
    c = 0
    ans = ""
    while m >= 0 or n >= 0 or c > 0:
        if m >= 0:
            c += int(a[m])
            m -= 1
        if n >= 0:
            c += int(b[n])
            n -= 1
        ans = str(c % 2) + ans
        c //= 2
    return ans


if __name__ == '__main__':
    print(addBinary2("11", "1"))
