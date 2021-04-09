# coding=utf-8
# author huxh
# time 2021/3/19 10:26 AM

# 查找连通分量的数量，最基础的并查集题目，也可以使用DFS、BFS实现


# dfs方法
def findCircleNum_dfs(isConnected: List[List[int]]) -> int:
    visited = set()

    def dfs(i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                dfs(j)

    res = 0
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i)
            res += 1
    return res


# bfs方法
def findCircleNum_bfs(isConnected: List[List[int]]) -> int:
    visited = set()
    res = 0

    for i in range(len(isConnected)):
        if i not in visited:
            q = [i]
            res += 1
            while q:
                cur = q.pop(0)
                visited.add(cur)
                for j in range(len(isConnected)):
                    if isConnected[cur][j] and j not in visited:
                        q.append(j)

    return res


# 并查集
def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    parent = list(range(n))

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        parent[find(i)] = find(j)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j]:
                union(i, j)

    return len([i for i in range(n) if parent[i] == i])
