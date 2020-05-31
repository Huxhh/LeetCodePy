# coding=utf-8
# author huxh
# time 2020/5/17 10:07 AM

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        import collections
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        res = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            u = q.popleft()
            res.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(res) != numCourses:
            res = list()
        return res
