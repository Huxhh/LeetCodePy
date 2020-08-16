# coding=utf-8
# author huxh
# time 2020/8/3 1:05 AM


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        maxs = 0
        end = 0
        for i in range(len(nums) - 1):
            if i + nums[i] > maxs:
                maxs = i + nums[i]
            if i == end:
                end = maxs
                steps += 1
        return steps
