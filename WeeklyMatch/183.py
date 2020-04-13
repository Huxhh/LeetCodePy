# coding=utf-8
# author huxh
# time 2020/4/5 10:17 AM


def minSubsequence(nums):
    s = sum(nums)
    nums = sorted(nums, reverse=True)
    res = []
    r = 0
    for n in nums:
        r += n
        res.append(n)
        if r > s - r:
            break
    return res


def numSteps(s):
    if s == '1':
        return 0

    s = list(s)
    steps = 0
    while len(s) != 1:
        if s[-1] == '0':
            s = s[:-1]
        else:
            index = len(s) - 1
            while index >= 0:
                if s[index] == '1':
                    s[index] = '0'
                    index -= 1
                else:
                    s[index] = '1'
                    break
            if index == -1:
                s = ['1'] + s[:]
        steps += 1
    return steps


def longestDiverseString(a, b, c):
    d = {}
    d['a'] = a
    d['b'] = b
    d['c'] = c
    res = ''
    keys = sorted(d, key=lambda x: d[x], reverse=True)

    while 1:
        flag = 0
        for k in keys:
            if d[k] == 0:
                flag += 1
        if flag >= 2:
            break

        if res and keys[0] == res[-1]:
            if d[keys[1]] <= 1:
                res += keys[1]
                d[keys[1]] -= 1
            else:
                res += keys[1] * 2
                d[keys[1]] -= 2
        else:
            if d[keys[0]] <= 1:
                res += keys[0]
                d[keys[0]] -= 1
            else:
                res += keys[0] * 2
                d[keys[0]] -= 2
            if d[keys[1]] > 0:
                res += keys[1]
                d[keys[1]] -= 1

        keys = sorted(d, key=lambda x: d[x],reverse=True)

    for k in d:
        if d[k] > 0 and res[-2] != k:
            if d[k] == 1:
                res += k
            else:
                res += k * 2

    return res




if __name__ == '__main__':
    # print(numSteps('1101'))
    print(longestDiverseString(0, 9, 12))
