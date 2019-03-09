# coding=utf-8


class Solution:
    def findCircleNum(self, M):
        n = len(M)
        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i]:
                continue
            else:
                self.dfs(M, i, visited)
                res += 1

        return res

    def dfs(self, M, k, visited):
        visited[k] = 1
        for i in range(len(M)):
            if not M[k][i] or visited[i]:
                continue
            self.dfs(M, i, visited)


def findCircleNum(M):
    n = len(M)
    res = 0
    visited = [0] * n
    q = []
    for i in range(n):
        if visited[i]:
            continue
        q.append(i)
        while q:
            t = q.pop(0)
            visited[t] = 1
            for j in range(n):
                if not M[t][j] or visited[j]:
                    continue
                q.append(j)
        res += 1

    return res

