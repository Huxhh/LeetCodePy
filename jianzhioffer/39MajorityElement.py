# coding=utf-8
# author huxh
# time 2020/3/28 10:09 PM


def majorityElement(nums):
    nums = sorted(nums)

    return nums[len(nums) // 2]


def majorityElement2(nums):
    cnt = 1
    cur = nums[0]
    for i in range(1, len(nums)):
        if cnt == 0:
            cur = nums[i]
        x = 1 if nums[i] == cur else -1
        cnt += x
    return cur


if __name__ == '__main__':
    print(majorityElement2([8,8,7,7,7]))