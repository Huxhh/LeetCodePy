# coding=utf-8


def myAtoi(str):
    s = str
    if s == "":
        return 0
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    res = 0
    flag = 1
    index = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            i += 1
        else:
            index = i
            break
    s = s[index:]
    if not (s[0] == '+' or s[0] == '-' or '0' <= s[0] <= '9'):
        return 0
    if len(s) > 2:
        if s[0] == '+' or s[0] == '-':
            if s[1] < '0' or s[1] > '9':
                return 0
    for i in range(0, len(s)):
        index = i
        if s[i] == ' ':
            return 0
        if s[i] == '-':
            flag *= -1
        if '0' <= s[i] <= '9':
            break
    s = s[index:]
    if len(s) > 0 and '0' <= s[0] <= '9':
        for char in s:
            if '0' <= char <= '9':
                res = res * 10 + (int(char) - int('0'))
            else:
                break

        res = flag * res
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN

        return res

    else:
        return 0


if __name__ == '__main__':
    s = "-42"
    print(myAtoi(s))