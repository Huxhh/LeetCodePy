# coding=utf-8


def longestValidParentheses(s):
    if s == "":
        return 0
    stack = []
    longest = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                if s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    if not stack:
        longest = len(s)
    else:
        a = len(s)
        b = 0
        while stack:
            b = stack[-1]
            stack.pop()
            longest = max(longest, a - b - 1)
            a = b
        longest = max(longest, a)

    return longest


def longestValidParentheses2(s):
    stack = []
    maxLen = 0
    last = -1
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if not stack:
                last = i
            else:
                stack.pop()
                if not stack:
                    maxLen = max(maxLen, i - last)
                else:
                    maxLen = max(maxLen, i - stack[-1])

    return maxLen


def longestValidParentheses3(s):
    stack = []
    maxlen = 0
    stack.append(-1)
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                maxlen = max(maxlen, i - stack[-1])
    return maxlen


def longestValidParentheses_dp(s):
    dp = [0] * len(s)
    longest = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                if i > 2:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] += 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                if i - dp[i - 1] >= 2:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2
        longest = max(longest, dp[i])
    return longest


if __name__ == '__main__':
    s = "()())"
    print(longestValidParentheses_dp(s))