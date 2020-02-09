# coding=utf-8

class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        def backtrack(n, first=0, curr=[]):
            output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(n, i + 1, curr)
                curr.pop()

        output = []
        backtrack(n)
        return output


def subsets(nums):
    res = [[]]
    for i in nums:
        res += [[i] + num for num in res]
    return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))
