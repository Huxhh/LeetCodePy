# -*- coding: utf-8 -*-


"""
思路
方法1：逐个判断字符串中字符，将结果加相应的值，当遇到特殊条件时，减去值 时间复杂度O(n) 空间复杂度O(1)
方法2：用一个dict存储字符与对应的值，后一位对应的值都应大于前一位，当后一位对应的值小于前一位的值时，减去当前的值
        时间复杂度O(n) 空间复杂度O(1)
方法3：用一个变量记录前一位的对应的值，当前一位的值小于当前位时，加上当前值并减去二倍的前一位的值
        时间复杂度O(n) 空间复杂度O(1)
"""


def romanToInt(s):
    ans = 0
    lens = len(s)
    for i in range(0, lens):
        if s[i] == 'I':
            if i != lens - 1:
                if s[i+1] == 'V':
                    ans -= 1
                elif s[i+1] == 'X':
                    ans -= 1
                else:
                    ans += 1
            else:
                ans += 1
        elif s[i] == 'V':
            ans += 5
        elif s[i] == 'X':
            if i != lens - 1:
                if s[i+1] == 'L':
                    ans -= 10
                elif s[i+1] == 'C':
                    ans -= 10
                else:
                    ans += 10
            else:
                ans += 10
        elif s[i] == 'L':
            ans += 50
        elif s[i] == 'C':
            if i != lens - 1:
                if s[i+1] == 'D':
                    ans -= 100
                elif s[i+1] == 'M':
                    ans -= 100
                else:
                    ans += 100
            else:
                ans += 100
        elif s[i] == 'D':
            ans += 500
        elif s[i] == 'M':
            ans += 1000

    return ans


def romanToInt2(s):
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    for i in range(0, len(s) - 1):
        if dic[s[i]] < dic[s[i+1]]:
            ans -= dic[s[i]]
        else:
            ans += dic[s[i]]
    ans += dic[s[len(s) - 1]]
    return ans


def romanToInt3(s):
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    M = 10000
    for x in s:
        m = dic[x]
        if m <= M:
            ans += m
        else:
            ans += (m - 2 * M)
        M = m
    return ans


if __name__ == '__main__':
    print(romanToInt3("LVIII"))