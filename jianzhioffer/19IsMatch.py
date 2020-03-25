# coding=utf-8
# author huxh
# time 2020/3/24 10:19 AM

# 递归
def isMatch(s, p):
    if not p:
        return not s

    first_match = bool(s) and p[0] in [s[0], '.']

    if len(p) >= 2 and p[1] == '*':
        return isMatch(s[1:], p) or first_match and isMatch(s, p[2:])
    else:
        return first_match and isMatch(s[1:], p[1:])

# 动态规划 O(TP) O(TP)
def isMatch2(s, p):
    mem = {}

    def dp(i, j):
        if (i, j) not in mem:
            if j == len(p):
                ans = i == len(s)
            else:
                first = i < len(s) and p[j] in ['.', s[i]]
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = first and dp(i + 1, j) or dp(i, j + 2)
                else:
                    ans = first and dp(i + 1, j + 1)
            mem[(i, j)] = ans
        return mem[(i, j)]

    return dp(0, 0)
