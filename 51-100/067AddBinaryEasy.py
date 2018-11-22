# coding=utf-8

def addBinary(a, b):
    n = len(a)
    m = len(b)
    ans = ""
    if n < m:
        a, b, m, n = b, a, n, m

    c = 0
    for i in range(m - 1, -1, -1):
        a[i] = chr(int(a[i]) + int(b[i]) + c)
        if int(a[i]) > 2:
            c = 1
    c = 0
    for i in range(n - 1, -1, -1):
        c = int(a[i]) // 2
        a[i] = chr((int(a[i]) + c) % 2)




if __name__ == '__main__':
    print(addBinary("110", "11"))