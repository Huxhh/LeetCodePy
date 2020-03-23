# coding=utf-8
# author huxh
# time 2020/3/21 12:28 PM

# 优化的暴力
def largestRectangleArea(heights):
    res = 0
    for i in range(len(heights)):
        mins = heights[i]
        for j in range(i, len(heights)):
            if heights[j] < mins:
                mis = heights[j]
            res = max(res, mis * (j - i + 1))
    return res

# 分治
def largestRectangleArea2(heights):

    def divide(l, r):
        if l >= r:
            return 0
        index = l
        for i in range(l, r + 1):
            if heights[i] < heights[index]:
                index = i

        return max(heights[index] * (r - l + 1), divide(l, index - 1), divide(index + 1, r))

    return divide(0, len(heights) - 1)


# 单调栈
def largestRectangleArea3(heights):
    res = 0
    s = [-1]
    for i in range(len(heights)):
        while s[-1] != -1 and heights[s[-1]] >= heights[i]:
            tmp = s.pop()
            res = max(res, heights[tmp] * (i - s[-1] - 1))
        s.append(i)
    while s[-1] != -1:
        tmp = s.pop()
        res = max(res, heights[tmp] * (len(heights) - s[-1] - 1))
    return res