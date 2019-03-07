# coding=utf-8


def getPermutation(n, k):
    nums = [str(i + 1) for i in range(0, n)]
    if k == 1:
        return ''.join(nums)

    fact = 1
    for i in range(2, n):
        fact *= i

    round = n - 1
    k -= 1
    res = []
    while round >= 0:
        index = k // fact
        k %= fact
        res.append(nums[index])
        nums.remove(nums[index])
        if round > 0:
            fact /= round
        round -= 1
    return ''.join(res)
