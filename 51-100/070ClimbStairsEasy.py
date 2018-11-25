# coding=utf-8

"""
思路：
方法一：暴力递归，会超时
方法二：在递归时发现会造成大量的重复计算，例如计算10时会计算9 8，计算9时会计算8 7，因此采用记忆搜索，在计算的同时使用数组保存每个
    中间过程的值存储下来，可以提高效率
方法三：动态规划，动态方程为mem[i] = mem[i - 1] + mem[i - 2]
    时间复杂度 O(n) 空间复杂度 O(n)
"""


def climbStairs(n):

    def getClimbStairs(x):
        if x == 1:
            return 1
        if x == 2:
            return 2

        return getClimbStairs(x - 1) + getClimbStairs(x - 2)

    return getClimbStairs(n)


def climbStairs2(n):
    mem = [-1] * (n + 1)

    def getClimbStairs(x, num):
        if x == 1:
            return 1
        if x == 2:
            return 2
        if num[x] == -1:
            num[x] = getClimbStairs(x - 1, num) + getClimbStairs(x - 2, num)
        return num[x]

    return getClimbStairs(n, mem)


def climbStairs3(n):
    mem = [-1] * (n + 1)
    mem[0] = 1
    mem[1] = 1

    for i in range(2, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]

    return mem[n]


if __name__ == '__main__':
    print(climbStairs3(35))