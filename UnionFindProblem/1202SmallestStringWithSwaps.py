# coding=utf-8
# author huxh
# time 2021/4/2 2:20 PM


class DisjointSetUnion:
    def __init__(self, n: int):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DisjointSetUnion(len(s))
        for x, y in pairs:
            dsu.unionSet(x, y)

        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[dsu.find(i)].append(ch)

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for i in range(len(s)):
            x = dsu.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()

        return "".join(ans)
