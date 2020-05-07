# coding=utf-8
# author huxh
# time 2020/4/18 2:54 PM


def minCount(coins):
    res = 0
    for num in coins:
        if num & 1:
            res += (num + 1) // 2
        else:
            res += num // 2
    return res


class Solution:
    def numWays(self, n, relation, k):
        re = {}
        for p in relation:
            if p[0] not in re:
                re[p[0]] = []
            re[p[0]].append(p[1])
        self.ans = 0

        def dfs(cur, curk):
            if curk == k:
                if cur == n - 1:
                    self.ans += 1
                return
            if cur not in re:
                return
            for des in re[cur]:
                dfs(des, curk + 1)
        dfs(0, 0)
        return self.ans


class Solution2:
    def getTriggerTime(self, increase, requirements):
        c, r, h = 0, 0, 0
        res = [-1] * len(requirements)
        total = [[c,r,h]]
        for i in range(len(increase)):
            c += increase[i][0]
            r += increase[i][1]
            h += increase[i][2]
            total.append([c,r,h])

        for i in range(len(requirements)):
            l = 0
            r = len(total) - 1
            mid = 0
            while l < r:
                mid = (l + r) // 2
                if total[mid][0] < requirements[i][0] and total[mid][1] < requirements[i][1] and total[mid][2] < requirements[i][2]:
                    l = mid + 1
                elif total[mid][0] >= requirements[i][0] and total[mid][1] >= requirements[i][1] and total[mid][2] >= requirements[i][2]:
                    r = mid
                else:
                    break

            for j in range(mid, r + 1):
                if res[i] < 0 and total[j][0] >= requirements[i][0] and total[j][1] >= requirements[i][1] and total[j][2] >= requirements[i][2]:
                    res[i] = j

        return res


class Solution3:
    def minJump(self, jump):
        vis = [0] * len(jump)
        des = [0] * len(jump)
        for i in range(len(des)):
            des[i] = i + jump[i]
        print(des)
        self.ans = float('inf')

        def bfs(cur, step):
            vis[cur] = 1
            if des[cur] >= len(jump):
                self.ans = min(self.ans, step + 1)
                return

            bfs(des[cur], step + 1)
            for i in range(0, cur):
                if not vis:
                    bfs(i, step + 1)
        bfs(0, 0)
        return self.ans



if __name__ == '__main__':
    # s = Solution2()
    # print(s.getTriggerTime([[0,4,5],[4,8,8],[8,6,1],[10,10,0]], [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]))
    s = Solution3()
    print(s.minJump([2,5,1,1,1,1]))