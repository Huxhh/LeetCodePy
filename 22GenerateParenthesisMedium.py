# coding=utf-8


class solution(object):
    def generateParenthesis(self, n):
        res = []
        strs = ""
        self.generateProcess(res, 0, 0, strs, n)
        return res

    def generateProcess(self, res, left, right, strs, n):
        if right > left or left > n or right > n:
            return
        if left == n and right == n:
            res.append(strs)
            return
        self.generateProcess(res, left + 1, right, strs + '(', n)
        self.generateProcess(res, left, right + 1, strs + ')', n)


def generateParenthesis2(n):
    res = []
    strs = ""
    def generateProcess(res, left, right, strs, n):
        if right > left or left > n or right > n:
            return
        if left == n and right == n:
            res.append(strs)
            return
        generateProcess(res, left + 1, right, strs + '(', n)
        generateProcess(res, left, right + 1, strs + ')', n)

    generateProcess(res, 0, 0, strs, n)
    return res


if __name__ == "__main":
    # s = solution()
    print(generateParenthesis2(2))
