# coding=utf-8

"""
思路：
方法一：暴力，找到所有子序列，会超时
    时间复杂度 O(n^2) 空间复杂度 O(1)
方法二：冬天；规划的思路，遍历一次，如果当前和大于0，继续加，否则与当前数字的和一定比当前数字小，再从当前数字开始加，每一个数字操作过后更新最大值
    时间复杂度 O(1) 空间复杂度O(1)
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


def maxSubArray3(nums):



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray2(nums))