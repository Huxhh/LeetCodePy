# coding=utf-8
# author huxh
# time 2020/4/25 9:42 AM


def permute(nums):
    res = []

    def back(tmp):
        if len(tmp) == len(nums):
            res.append(tmp[:])
        else:
            for i in range(len(nums)):
                if nums[i] not in tmp:
                    tmp.append(nums[i])
                    back(tmp)
                    tmp.pop()
    back([])
    return res


def permute2(nums):
    res = []

    def back(first):
        if first == len(nums):
            res.append(nums[:])
        else:
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                back(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

    back(0)
    return res
