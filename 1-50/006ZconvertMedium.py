# coding=utf-8


def convert(s, numRows):
    if numRows == 1:
        return s

    total_list = []
    for i in range(numRows):
        total_list.append([])

    row_num = 0
    going_down = True
    for cha in s:
        total_list[row_num] += cha
        if row_num == 0:
            going_down = True
        if row_num == numRows - 1:
            going_down = False
        if going_down:
            row_num += 1
        else:
            row_num -= 1
    ans = []
    for st in total_list:
        ans += st

    return ''.join(ans)


def convert2(s, numRows):
    if numRows == 1:
        return s

    ans = []
    n = len(s)
    cycle = 2 * numRows - 2

    for i in range(numRows):
        j = 0
        while j + i < n:
            ans += s[j + i]

            if i != 0 and i != numRows - 1 and j + cycle - i < n:
                ans += s[j + cycle - i]
            j += cycle

    return ''.join(ans)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(convert2(s, numRows))