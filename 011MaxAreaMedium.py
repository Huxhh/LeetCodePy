# coding=utf-8

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