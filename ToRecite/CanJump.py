# coding=utf-8
# author huxh
# time 2020/8/3 1:01 AM


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        maxs = 0
        while i < n and i <= maxs:
            maxs = max(i + nums[i], maxs)
            i += 1
        return i == n


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

