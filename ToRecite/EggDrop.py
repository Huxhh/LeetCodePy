# coding=utf-8
# author huxh
# time 2020/8/2 7:31 PM


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        mem = {}
        def dp(k, n):
            if (k, n) not in mem:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    l = 1
                    r = n
                    while l + 1 < r:
                        mid = (l + r) // 2
                        broke = dp(k - 1, mid - 1)
                        not_broke = dp(k, n - mid)
                        if broke < not_broke:
                            l = mid
                        elif broke > not_broke:
                            r = mid
                        else:
                            l = r = mid
                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (l, r))
                mem[(k, n)] = ans
            return mem[(k, n)]

        return dp(K, N)
