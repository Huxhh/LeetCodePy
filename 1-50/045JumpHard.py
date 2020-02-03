# coding=utf-8

def jump(nums):
    steps = 0
    maxs = 0
    end = 0
    for i in range(len(nums) - 1):
        maxs = max(maxs, nums[i] + i)
        if i == end:
            end = maxs
            steps += 1
    return steps


# 在最坏情况[1,1,1,1,1...]会超时
def jump2(nums):
    pos = len(nums) - 1
    steps = 0
    while pos != 0:
        for i in range(pos):
            if nums[i] >= pos - i:
                pos = i
                steps += 1
                break
    return steps



if __name__ == '__main__':
    nums = [5,4,3,2,1,1]
    print(jump2(nums))