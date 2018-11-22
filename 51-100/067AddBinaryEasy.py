# coding=utf-8

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


if __name__ == '__main__':
    print(addBinary("1010", "1011"))
