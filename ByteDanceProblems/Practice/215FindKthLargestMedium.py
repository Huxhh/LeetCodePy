# coding=utf-8
# author huxh
# time 2020/7/5 4:40 PM


class Solution:
    def findKthLargest(self, nums, k):
        return self.quick_sort(nums, 0, len(nums) - 1, k)

    def quick_sort(self, nums, left, right, k):
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
                return self.quick_sort(nums, l + 1, right, k - index)
            else:
                return self.quick_sort(nums, left, l - 1, k)
        else:
            return pivot


