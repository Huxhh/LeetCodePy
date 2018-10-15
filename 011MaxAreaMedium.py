# coding=utf-8


"""
思路
方法一：暴力法  遍历每一对边，计算所能容纳的面积，最大的即为所求
    时间复杂度 O(n^2) 空间复杂度 O(1) ps.python使用暴力法会超时
方法二：双指针法  两个指针，一个在开始，一个在末尾，计算面积，然后将两条边中较短的一条想中心移动，
    同时维护maxArea，直到两条边碰到，具体解释可以参考：
    https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm
    即没有计算的点的面积一定比路径上的点代表的面积小，因此只需要找到路线上面积最大的点
    时间复杂度 O(n) 空间复杂度 O(1)
"""


def maxArea(height):
    max_area = 0
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
    return max_area


def maxArea2(height):
    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea2(height))