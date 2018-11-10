# coding=utf-8


def multiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    ans = [0] * (len1 + len2)

    for i in reversed(range(len1)):
        for j in reversed(range(len2)):
            res = int(num1[i]) * int(num2[j])
            ans[i + j + 1] += res
            ans[i + j] += ans[i + j + 1] // 10
            ans[i + j + 1] %= 10

    i = 0
    while i < len(ans) and ans[i] == 0:
        i += 1
    ret = ''.join([str(num) for num in ans[i:]])
    if ret:
        return ret
    else:
        return '0'


if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print(multiply(num1, num2))