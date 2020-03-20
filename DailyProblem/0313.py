# coding=utf-8


def majorityElement(nums):
    cnt = 1
    res = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != res:
            if cnt > 0:
                cnt -= 1
            else:
                res = nums[i]
        else:
            cnt += 1
    return res




if __name__ == '__main__':
    print(majorityElement([2,2,1,1,1,2,2]))
