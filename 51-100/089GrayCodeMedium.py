# coding=utf-8

"""
思路
理解格雷码的计算方式：首位1不变，后面剩余的位依次与前一位异或得到
"""

def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [i ^ (i >> 1) for i in range(1 << n)]


if __name__ == '__main__':
    print(grayCode(2))