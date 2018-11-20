# coding=utf-8

"""
思路：
仅需处理特殊情况即[9,9,9,9...]的情况
时间复杂度 O(n) 空间复杂度 O(1)
"""

def plusOne(digits):
    ans = [0] * (len(digits) + 1)

    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        flag = 0
        index = 0
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                flag = 1
                index = i
                break
            i -= 1
        if flag:
            digits[index] += 1
            digits[index + 1:] = [0] * (len(digits[index:]) - 1)
            return digits
        else:
            ans[0] = 1

    return ans


def plusOne2(digits):
    n = len(digits)
    digits[n - 1] += 1
    for i in range(n - 1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
    if digits[0] == 10:
        digits[0] = 0
        digits = [1] + digits
    return digits

if __name__ == '__main__':
    print(plusOne2([2, 9,3,9]))