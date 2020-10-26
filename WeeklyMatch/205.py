# coding=utf-8
# author huxh
# time 2020/9/6 10:27 AM


def modifyString(s):
    if s == '?':
        return 'a'
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    res = ''
    for i in range(len(s)):
        if s[i] != '?':
            res += s[i]
        else:
            if i == len(s) - 1:
                for item in l:
                    if item != res[-1]:
                        res += item
                        break
            elif i == 0:
                for item in l:
                    if item != s[i + 1]:
                        res += item
                        break
            else:
                for item in l:
                    if item != res[-1] and item != s[i + 1]:
                        res += item
                        break
    return res


def numTriplets(nums1, nums2):

    def get_count(n1, n2):
        d = {}
        res = 0
        for i in range(len(n2) - 1):
            for j in range(i + 1, len(n2)):
                cur = n2[i] * n2[j]
                if cur not in d:
                    d[cur] = 0
                d[cur] += 1

        for i in range(len(n1)):
            cur = n1[i] ** 2
            if cur in d:
                res += d[cur]
        return res
    return get_count(nums1, nums2) + get_count(nums2, nums1)


def minCost(s, cost):
    if len(s) == 1:
        return 0
    res = 0
    i = 0
    j = 0
    tmp_cost = 0
    while i < len(s):
        while s[i] == s[j] and j < len(s):
            tmp_cost = max(tmp_cost, cost[j])
            j += 1
        if j - i > 1:
            cur_cost = sum(cost[i:j])
            res += (cur_cost - tmp_cost)
        i = j
        tmp_cost = 0
    return res
