# coding=utf-8
# author huxh
# time 2020/4/7 9:54 AM


def maxSlidingWindow(nums, k):
    if not nums:
        return []

    q = []
    res = []
    for i in range(len(nums)):
        if i >= k and q[0] == nums[i - k]:
            q.pop(0)

        while q and q[-1] < nums[i]:
            q.pop()
        q.append(nums[i])

        if i >= k - 1:
            res.append(q[0])

    return res


from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        res = []
        dq = deque()
        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i - dq[0] > k - 1:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
