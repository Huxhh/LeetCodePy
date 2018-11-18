# coding=utf-8


def threeSum(nums):
    res = []
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = []
                    tmp.append(nums[i])
                    tmp.append(nums[j])
                    tmp.append(nums[k])
                    tmp = sorted(tmp)
                    if tmp not in res:
                        res.append(tmp)

    return res


def threeSum2(nums):
    n = len(nums)
    res = []
    if n < 3:
        return res

    nums = sorted(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = n - 1
        target = -nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[l], nums[r], nums[i]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return res


def threeSum3(nums):
    nums_hash = {}
    result = list()
    for num in nums:
        nums_hash[num] = nums_hash.get(num, 0) + 1
    if 0 in nums_hash and nums_hash[0] >= 3:
        result.append([0, 0, 0])

    neg = list(filter(lambda x: x < 0, nums_hash))
    pos = list(filter(lambda x: x >= 0, nums_hash))

    for i in neg:
        for j in pos:
            dif = 0 - i - j
            if dif in nums_hash:
                if dif in (i, j) and nums_hash[dif] >= 2:
                    result.append([i, j, dif])
                if dif < i or dif > j:
                    result.append([i, j, dif])

    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum2(nums))