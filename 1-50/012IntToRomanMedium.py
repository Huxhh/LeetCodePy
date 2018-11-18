# coding=utf-8


def intToRoman(num):
    ans = ''
    m_num = num // 1000
    num = num % 1000
    ans += 'M' * m_num
    b_num = num // 100
    if b_num == 4 or b_num == 9:
        if b_num == 4:
            ans += 'CD'
        else:
            ans += 'CM'
    else:
        bd_num = b_num // 5
        ans += bd_num * 'D'
        bc_num = b_num % 5
        ans += bc_num * 'C'
    num %= 100
    s_num = num // 10
    if s_num == 4 or s_num == 9:
        if s_num == 4:
            ans += 'XL'
        else:
            ans += 'XC'
    else:
        sl_num = s_num // 5
        ans += sl_num * 'L'
        sx_num = s_num % 5
        ans += sx_num * 'X'
    num %= 10
    g_num = num
    if g_num == 4 or g_num == 9:
        if g_num == 4:
            ans += 'IV'
        else:
            ans += 'IX'
    else:
        gv_num = g_num // 5
        ans += gv_num * 'V'
        gi_num = g_num % 5
        ans += gi_num * 'I'

    return ans


def intToRoman2(num):
    res = ''
    token = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    for n, t in token:
        while num >= n:
            res += t
            num -= n
    return res


if __name__ == '__main__':
    print(intToRoman2(1994))