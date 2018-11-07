# coding=utf-8


def threeSumClosest(nums, target):
    n = len(nums)
    res = 0
    min_d = 1000000
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if abs(nums[i] + nums[j] + nums[k] - target) < min_d:
                    min_d = abs(nums[i] + nums[j] + nums[k] - target)
                    res = nums[i] + nums[j] + nums[k]

    return res


def threeSumClosest2(nums, target):
    n = len(nums)
    nums = sorted(nums)
    min_d = 100000000
    res = 0
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = n - 1
        t = nums[i]

        while l < r:
            if abs(t + nums[l] + nums[r] - target) < min_d:
                min_d = abs(t + nums[l] + nums[r] - target)
                res = t + nums[l] + nums[r]

            if t + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return res


if __name__ == '__main__':
    nums = [1,1,-1,-1,3]
    target = -1
    print(threeSumClosest2(nums, target))
