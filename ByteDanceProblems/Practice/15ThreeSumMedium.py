# coding=utf-8
# author huxh
# time 2020/7/5 10:08 PM


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)

        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            b = len(nums) - 1
            target = - nums[i]
            for c in range(i + 1, len(nums)):
                if c > i + 1 and nums[c] == nums[c - 1]:
                    continue

                while c < b and nums[c] + nums[b] > target:
                    b -= 1
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    res.append([nums[i], nums[b], nums[c]])
        return res
