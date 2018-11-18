# coding=utf-8


def nextPermutation(nums):
    n = len(nums) - 2
    while n >= 0 and nums[n] >= nums[n + 1]:
        n -= 1
    if n >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[n]:
            j -= 1

        temp = nums[j]
        nums[j] = nums[n]
        nums[n] = temp

    end = nums[n + 1:]
    end.reverse()
    nums[n + 1:] = end[:]


if __name__ == '__main__':
    nums = [3,2,1]
    nextPermutation(nums)
    print(nums)