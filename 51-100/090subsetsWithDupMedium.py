# coding=utf-8

class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        def backtrack(n, first=0, curr=[]):
            if curr[:] not in output:
                output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(n, i + 1, curr)
                curr.pop()

        output = []
        backtrack(n)
        return output


def subsetsWithDup(nums):
    nums.sort()
    res = [[]]
    # for i in nums:
    #     res += [[i]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            res += [[nums[i]] + k for k in res]

    return res


class Solution2(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        self.res = []
        self.dfs(0, nums, [])
        return self.res

    def dfs(self, pos, nums, cur):
        self.res.append(cur[:])
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]:
                continue

            cur.append(nums[i])
            self.dfs(i + 1, nums, cur)
            cur.pop()


if __name__ == '__main__':
    nums = [2,1,2]
    s = Solution2()
    print(s.subsetsWithDup(nums))

