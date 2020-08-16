# coding=utf-8
# author huxh
# time 2020/8/2 9:37 PM


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.qs(nums, 0, len(nums) - 1, k)

    def qs(self, nums, left, right, k):
        l = left
        r = right
        pivot = nums[right]

        if left < right:
            while l < r:
                while l < r and nums[l] >= pivot:
                    l += 1
                nums[r] = nums[l]
                while l < r and nums[r] < pivot:
                    r -= 1
                nums[l] = nums[r]
            nums[l] = pivot
            index = l - left + 1
            if index == k:
                return pivot
            elif index < k:
                return self.qs(nums, l + 1, right, k - index)
            else:
                return self.qs(nums, left, l - 1, k)
        else:
            return pivot
