# coding=utf-8


def isMatch(s, p):
    if not p:
        return not s

    first = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return isMatch(s, p[2:]) or first and isMatch(s[1:], p)
    else:
        return first and isMatch(s[1:], p[1:])


def isMatch2(s, p):
    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            if j == len(p):
                ans = i == len(s)
            else:
                first = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = dp(i, j + 2) or first and dp(i + 1, j)
                else:
                    ans = first and dp(i + 1, j + 1)
            memo[(i, j)] = ans

        return memo[(i, j)]
    return dp(0, 0)


if __name__ == '__main__':
    print(isMatch('aa', 'b.'))
