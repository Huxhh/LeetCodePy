# coding=utf-8


class Solution:
    def findKthLargest(self, nums, k):
        # self.quick_sort(nums, 0, len(nums) - 1)
        return self.quick_sort2(nums, 0, len(nums) - 1, k)
        # return nums[k - 1]

    def quick_sort(self, nums, left, right):
        if left >= right:
            return

        l = left
        r = right
        key = nums[left]
        while l < r:
            while l < r and nums[r] < key:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] >= key:
                l += 1
            nums[r] = nums[l]

        nums[l] = key
        self.quick_sort(nums, left, l - 1)
        self.quick_sort(nums, l + 1, right)

    def quick_sort2(self, nums, left, right, k):
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
                return self.quick_sort2(nums, l + 1, right, k - index)
            else:
                return self.quick_sort2(nums, left, l - 1, k)
        else:
            return pivot

if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(s.findKthLargest(nums, k))
