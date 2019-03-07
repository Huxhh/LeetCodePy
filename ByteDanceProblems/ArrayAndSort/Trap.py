# coding=utf-8

def trap(height):
    area = 0

    idx = 0
    for i in range(0, len(height)):
        if height[i] > height[idx]:
            idx = i

    lheight = 0
    rheight = 0
    for i in range(0, idx):
        if height[i] < lheight:
            area += lheight - height[i]
        else:
            lheight = height[i]

    for i in range(len(height) - 1, idx, -1):
        if height[i] < rheight:
            area += rheight - height[i]
        else:
            rheight = height[i]

    return area


def trap2(height):
    area = 0
    left = 0
    right = len(height) - 1
    lheight = 0
    rheight = 0
    while left < right:
        if height[left] < height[right]:
            if lheight <= height[left]:
                lheight = height[left]
            else:
                area += lheight - height[left]
            left += 1
        else:
            if rheight <= height[right]:
                rheight = height[right]
            else:
                area += rheight - height[right]
            right -= 1

    return area