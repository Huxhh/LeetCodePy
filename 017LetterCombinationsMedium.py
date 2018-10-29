# coding=utf-8


"""
思路：
方法一：递归，使用长度控制返回，具体见代码
    时间复杂度 O(n^2) 空间复杂度 O(n)
方法二：循环，将当前每一个数字对应的字符加到res中每一个字符串后面
    时间复杂度 O(n^2) 空间复杂度 O(n^2)
"""


def letterCombinations(digits):
    dic = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    ret = []
    if not digits:
        return ret

    def backtrack(pre, length, res, dig):
        if length == len(dig):
            res.append(pre)
            return
        num = dig[length]
        letters = dic[num]
        for i in letters:
            backtrack(pre+i, length + 1, res, dig)

    backtrack('', 0, ret, digits)

    return ret


def letterCombinations2(digits):
    dic = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    if not digits:
        return []
    res = ['']
    for i in range(len(digits)):
        letters = dic[digits[i]]
        tmp = []
        for l in letters:
            for r in res:
                r = r + l
                tmp.append(r)
        res = tmp[:]

    return res


if __name__ == '__main__':
    d = "23"
    print(letterCombinations2(d))