# coding=utf-8
import functools

def maxEnvelopes(envelopes):
    if not envelopes:
        return 0
    res = 0
    dp = [1] * len(envelopes)
    envelopes = sorted(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(dp[i], res)

    return res



class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        dp = []
        envelopes = sorted(envelopes, key=functools.cmp_to_key(self.comp))
        print(envelopes)
        for i in range(len(envelopes)):
            left = 0
            right = len(dp)
            t = envelopes[i][1]
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < t:
                    left = mid + 1
                else:
                    right = mid

            if right >= len(dp):
                dp.append(t)
            else:
                dp[right] = t

        return len(dp)

    def comp(self, x, y):
        if x[0] == y[0]:
            if x[1] > y[1]:
                return -1
            else:
                return 1
        else:
            if x[0] < y[0]:
                return -1
            else:
                return 1


if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    s = Solution()
    s.maxEnvelopes(envelopes)
