# coding=utf-8
# author huxh
# time 2020/8/2 7:00 PM


class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        def robber(tmp):
            if not tmp:
                return 0
            if len(tmp) == 1:
                return tmp[0]

            first = tmp[0]
            second = max(tmp[0], tmp[1])
            for i in range(2, len(tmp)):
                first, second = second, max(tmp[i] + first, second)
            return second

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(robber(nums[1:]), robber(nums[:-1]))
