# coding=utf-8


def permuteUnique(nums):
    ans = []
    nums = sorted(nums)
    used = [0] * len(nums)

    def backtrack(ans, temp, nums, used):
        if len(temp) == len(nums):
            ans.append(temp[:])
        else:
            for i in range(0, len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and (not used[i - 1])):
                    continue
                else:
                    used[i] = 1
                    temp.append(nums[i])
                    backtrack(ans, temp, nums, used)
                    used[i] = 0
                    temp.pop()

    backtrack(ans, [], nums, used)

    return ans


if __name__ == '__main__':
    nums = [2, 2, 1, 1]
    print(permuteUnique(nums))