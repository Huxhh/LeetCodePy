# coding=utf-8
# author huxh
# time 2020/8/2 11:27 PM

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
