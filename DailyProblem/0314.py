# coding=utf-8

def lengthOfLIS(nums):
    if not nums:
        return 0

    dp = [0] * len(nums)
    dp[0] = 1
    ans = 1
    for i in range(1, len(nums)):
        tm = 0
        for j in range(i):
            if nums[i] > nums[j]:
                tm = max(tm, dp[j])

        dp[i] = tm + 1
        ans = max(ans, dp[i])


    return ans


def lengthOfLIS2(nums):
    if not nums:
        return 0

    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            l = 0
            r = len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            d[loc] = n
    return len(d)



if __name__ == '__main__':
    print(lengthOfLIS2([10,9,2,5,3,7,101,18]))