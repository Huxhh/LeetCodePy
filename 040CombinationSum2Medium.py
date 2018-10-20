# coding=utf-8


def combinationSum2(candidates, target):
    sorted_candidates = sorted(candidates)
    res = []

    def backtrack(bt_candidates, start, target, temp, res):
        if target == 0:
            res.append(temp[:])
            return
        if target < 0:
            return
        for i in range(start, len(bt_candidates)):
            if i > start and bt_candidates[i] == bt_candidates[i - 1]:
                continue
            temp.append(bt_candidates[i])
            backtrack(bt_candidates, i + 1, target - bt_candidates[i], temp, res)
            temp.pop()

    backtrack(sorted_candidates, 0, target, [], res)

    return res


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(combinationSum2(candidates, target))