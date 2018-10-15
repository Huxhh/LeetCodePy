# coding=utf-8


class Solution(object):
    def combinationSum(self, candidates, target):
        sorted_candidates = sorted(candidates)
        res = []
        self.backtrack(sorted_candidates, 0, target, [], res)
        return res

    def backtrack(self, bt_sorted_candidates, start, target, temp, res):
        if target == 0:
            res.append(temp[:])
            return
        if target < 0:
            return
        for i in range(start, len(bt_sorted_candidates)):
            temp.append(bt_sorted_candidates[i])
            self.backtrack(bt_sorted_candidates, i, target - bt_sorted_candidates[i], temp, res)
            temp.pop()


def combinationSum(candidates, target):
    sorted_candidates = sorted(candidates)
    res = []

    def backtrack(bt_candidates, start, target, temp, res):
        if target == 0:
            res.append(temp[:])
            return
        if target < 0:
            return
        for i in range(start, len(bt_candidates)):
            temp.append(bt_candidates[i])
            backtrack(bt_candidates, i, target - bt_candidates[i], temp, res)
            temp.pop()

    backtrack(sorted_candidates, 0, target, [], res)

    return res


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    # s = Solution()
    # print(s.combinationSum(candidates, target))
    print(combinationSum(candidates, target))


