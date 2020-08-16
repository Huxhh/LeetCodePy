# coding=utf-8
# author huxh
# time 2020/8/2 5:44 PM

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp_i2 = 0
        dp_i1 = 0
        for i in range(2, len(nums) + 2):
            tmp = dp_i1
            dp_i1 = max(dp_i2 + nums[i - 2], dp_i1)
            dp_i2 = tmp
        return dp_i1


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second

