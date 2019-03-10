# coding=utf-8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        return self.divi(nums, 0, len(nums) - 1)

    def divi(self, nums, l, r):
        if l > r:
            return -99999
        if l == r:
            return nums[l]

        mid = (l + r) // 2
        left = self.divi(nums, l, mid - 1)
        right = self.divi(nums, mid + 1, r)
        t = nums[mid]
        maxres = nums[mid]
        for i in range(mid - 1, l - 1, -1):
            t += nums[i]
            maxres = max(t, maxres)
        t = maxres
        for i in range(mid + 1, r + 1):
            t += nums[i]
            maxres = max(t, maxres)

        return max(max(left, right), maxres)



