# coding=utf-8

def longestConsecutive(nums):
    d = {}
    for i in nums:
        d[i] = 0

    maxLength = 0
    for num in nums:
        if num in d:
            count = 1
            # del d[num]
            d.pop(num)

            low = num - 1
            while low in d:
                # del d[low]
                d.pop(low)
                count += 1
                low -= 1

            high = num + 1
            while high in d:
                # del d[high]
                d.pop(high)
                count += 1
                high += 1

            maxLength = max(maxLength, count)

    return maxLength
