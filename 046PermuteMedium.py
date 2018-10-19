# coding=utf-8


def permute(nums):
    ans = []

    def backtrack(ans, temp, nums):
        if len(temp) == len(nums):
            ans.append(temp[:])
        else:
            for i in range(0, len(nums)):
                if nums[i] in temp:
                    continue
                else:
                    temp.append(nums[i])
                    backtrack(ans, temp, nums)
                    temp.pop()

    backtrack(ans, [], nums)

    return ans


if __name__ == '__main__':
    nums = [1,2,3]
    print(permute(nums))
