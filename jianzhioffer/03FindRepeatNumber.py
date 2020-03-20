# coding=utf-8


# 时间O(N) 空间O(1)
def findRepeatNumber(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]:
                return nums[i]

            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


# 同上
def findRepeatNumber2(nums):
    for i in range(len(nums)):
        if nums[i] == i:
            continue
        if nums[i] != i and nums[nums[i]] == nums[i]:
            return nums[i]
        while nums[i] != i:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


# 时间O(N) 空间O(1)
def findRepeatNumber3(nums):
    s = set()
    for n in nums:
        if n in s:
            return n
        s.add(n)
