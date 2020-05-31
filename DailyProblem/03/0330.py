# coding=utf-8
# author huxh
# time 2020/3/30 10:10 AM


def lastRemaining(n, m):
    if n == 1:
        return 0

    vis = [0] * n
    cnt = 0
    index = 0
    while sum(vis) != n - 1:
        if index >= n:
            index %= n
        if vis[index]:
            index += 1
            continue
        else:
            cnt += 1
            if cnt == m:
                cnt = 0
                vis[index] = 1
        index += 1

    for i in range(n):
        if not vis[i]:
            return i


sys.setrecursionlimit(100000)

def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)


class Solution2:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f





if __name__ == '__main__':
    print(lastRemaining(5, 3))
