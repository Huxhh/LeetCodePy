# coding=utf-8

"""
思路：
方法一：暴力，找到所有子序列，会超时
    时间复杂度 O(n^2) 空间复杂度 O(1)
方法二：动态规划的思路，遍历一次，如果当前和大于0，继续加，否则与当前数字的和一定比当前数字小，再从当前数字开始加，每一个数字操作过后更新最大值
    时间复杂度 O(n) 空间复杂度O(1)
方法三：假设数组下标有效范围是l到r,将数组分为左半部分下标为（l，mid-1）和右半部分下标为(mid+1，r)以及中间元素下标为mid，
    接下来递归求出左半部分的最大子序和：left=helper(nums,l,mid-1); 右半部分最大子序和right=helper(nums,mid+1,r);接下来再将左半部分
    右边界，右半部分左边界以及中间元素nums[mid]整合，用了两个循环，先整合左半部分右边界和中间值，再将整合结果与右半部分左边界整合得到整合以后
    的最大子序和max_num，最后返回max_num，left,right的最大值即是要求的最大子序和。
    时间复杂度 O(nlogn) 空间复杂度 O(1)
"""


def maxSubArray(nums):
    ans = -2147483647
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            summary = sum(nums[i:j])
            ans = max(ans, summary)

    return ans


def maxSubArray2(nums):
    res = nums[0]
    summary = 0
    for num in nums:
        if summary > 0:
            summary += num
        else:
            summary = num
        res = max(res, summary)

    return res


class Solution:
    def maxSubArray3(self, nums):
        return self.divide(nums, 0, len(nums) - 1)

    def divide(self, nums, l, r):
        if l == r:
            return nums[l]
        # if l == r - 1:
        #     return max(nums[l], max(nums[r], nums[l]+nums[r]))
        if l > r:
            return -2147483648

        mid = (l + r) // 2
        l_max = self.divide(nums, l, mid - 1)
        r_max = self.divide(nums, mid + 1, r)
        max_num = nums[mid]
        tmp = nums[mid]
        i = mid - 1
        while i >= l:
            tmp += nums[i]
            max_num = max(max_num, tmp)
            i -= 1
        tmp = max_num
        i = mid + 1
        while i <= r:
            tmp += nums[i]
            max_num = max(max_num, tmp)
            i += 1
        return max(max(l_max, r_max), max_num)




if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray3(nums))