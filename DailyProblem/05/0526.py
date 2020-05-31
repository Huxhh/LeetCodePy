# coding=utf-8
# author huxh
# time 2020/5/26 10:07 AM


def findDuplicate(nums):
    slow = 0
    fast = 0
    while 1:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


def findDuplicate2(nums):
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        mid = (l + r) // 2

        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1

        if cnt > mid:
            r = mid
        else:
            l = mid + 1
    return l
