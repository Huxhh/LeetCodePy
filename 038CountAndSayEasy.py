# coding=utf-8


"""
思路
使用strs字符串保存上一次的结果，然后对strs进行分析，依次遍历字符，看当前字符是否与下一个字符相等，若相等则nums记数加一，
若不相等，则将当前记数的nums与当前字符str[i]合并输出到返回字符串ret，最后处理最后一个字符，将它和倒数第二个字符比较

另：考虑递归实现
"""


def countAndSay(n):
    x = 1
    strs = "1"
    ret = ""
    if n == 1:
        return strs
    while x < n:
        ret = ""
        nums = 1
        if len(strs) == 1:
            ret = '1' + strs[0]
        else:
            for i in range(0, len(strs) - 1):
                if strs[i] == strs[i + 1]:
                    nums += 1
                else:
                    ret = ret + str(nums) + strs[i]
                    nums = 1
            if strs[-1] == strs[-2]:
                ret = ret + str(nums) + strs[-1]
            else:
                ret = ret + '1' + strs[-1]
        x += 1
        strs = ret

    return ret


def countAndSay2(s, depth, n):
    if depth == n:
        return s
    ans = ""
    x = 1
    s += "A"
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            x += 1
        else:
            ans = ans + str(x) + s[i]
            x = 1
    if x != 1:
        ans = ans + str(x) + str[-1]

    return countAndSay2(ans, depth + 1, n)


if __name__ == '__main__':
    print(countAndSay2("1", 1, 5))
