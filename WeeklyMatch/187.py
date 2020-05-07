# coding=utf-8
# author huxh
# time 2020/5/3 10:16 AM


def destCity(paths):
    s = set()
    for p in paths:
        s.add(p[0])
        s.add(p[1])

    for p in paths:
        s.remove(p[0])
    return list(s)[0]


def kLengthApart(nums, k):
    pre_index = -1
    for i in range(len(nums)):
        if nums[i] == 1:
            if pre_index == -1:
                pre_index = i
                continue
            else:
                if i - pre_index <= k:
                    return False
                pre_index = i
    return True


def longestSubarray(nums, limit):
    if len(nums) == 1:
        return 1

    maxq = [nums[0]]
    minq = [nums[0]]
    i, j = 0, 1
    n = len(nums)
    res = 0
    while i < n and j < n + 1:
        if maxq[0] - minq[0] <= limit:
            res = max(res, j - i)
            if j == n:
                break
            while maxq and maxq[-1] < nums[j]:
                maxq.pop()
            maxq.append(nums[j])
            while minq and minq[-1] > nums[j]:
                minq.pop()
            minq.append(nums[j])
            j += 1
        else:
            if nums[i] == maxq[0]:
                maxq.pop(0)
            if nums[i] == minq[0]:
                minq.pop(0)
            i += 1
    return res


def longestSubarray2(nums, limit):
    if len(nums) == 1:
        return 1

    maxq = [0]
    minq = [0]
    i, j = 0, 1
    n = len(nums)
    res = 0
    while i < n and j < n:
        if nums[maxq[0]] - nums[minq[0]] <= limit:
            while maxq and nums[maxq[-1]] < nums[j]:
                maxq.pop()
            maxq.append(j)
            while minq and nums[minq[-1]] > nums[j]:
                minq.pop()
            minq.append(j)
            j += 1
        else:
            if minq[0] == i:
                minq.pop(0)
            if maxq[0] == i:
                maxq.pop(0)
            i += 1
        if nums[maxq[0]] - nums[minq[0]] <= limit:
            res = max(res, j - i)
    return res


if __name__ == '__main__':
    print(longestSubarray2([8,2,4,7], 4))
