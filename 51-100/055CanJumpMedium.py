# coding=utf-8


def canJump(nums):
    n = len(nums)
    i = 0
    reach = 0
    while i < n and i <= reach:
        reach = max(reach, i + nums[i])
        i += 1

    return i == n


def canJump2(nums):
    length = len(nums)
    if length == 1:
        return True
    steps_require = 1
    i = length - 2
    while i >= 0:
        if nums[i] >= steps_require:
            steps_require = 0
        steps_require += 1
        i -= 1
    return steps_require == 1


if __name__ == '__main__':
    nums = [3,2,1,0,4]
    print(canJump2(nums))