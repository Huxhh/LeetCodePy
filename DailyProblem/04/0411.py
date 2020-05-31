# coding=utf-8
# author huxh
# time 2020/4/11 11:33 AM


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        d = {}

        def dp(K, N):
            if N == 0:
                return 0
            if K == 1:
                return N
            if (K, N) in d:
                return d[(K, N)]
            res = float('INF')
            # for i in range(1, N + 1):
            #     res = min(res, max(dp(K, N - i), dp(K - 1, i - 1)) + 1)
            l = 1
            r = N
            while l <= r:
                mid = (l + r) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    r = mid - 1
                    res = min(res, broken + 1)
                else:
                    l = mid + 1
                    res = min(res, not_broken + 1)

            d[(K, N)] = res
            return res

        return dp(K, N)
