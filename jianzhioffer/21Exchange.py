# coding=utf-8
# author huxh
# time 2020/3/24 10:44 AM


def exchange(nums):
    if not nums:
        return []

    l = 0
    r = len(nums) - 1
    while l < r:
        while l < r and nums[l] & 1:
            l += 1

        while l < r and not nums[r] & 1:
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]
    return nums

def exchange2(nums):
    if not nums:
        return []

    l = 0
    r = 0
    while r < len(nums):
        if nums[r] & 1:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
        r += 1
    return nums

if __name__ == '__main__':
    print(exchange2([1,3,4,6,7,9]))