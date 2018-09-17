# coding=utf-8


def merge(nums1, m, nums2, n):
    index = m + n - 1
    x = m - 1
    y = n - 1
    while True:
        if x < 0 and y < 0:
            break
        if x >= 0 and y >= 0:
            if nums1[x] >= nums2[y]:
                nums1[index] = nums1[x]
                x -= 1
            else:
                nums1[index] = nums2[y]
                y -= 1
            index -= 1
        elif x >= 0 > y:
            nums1[index] = nums1[x]
            x -= 1
            index -= 1
        elif x < 0 <= y:
            nums1[index] = nums2[y]
            y -= 1
            index -= 1

    return nums1


def merge2(nums1, m, nums2, n):
    index = m + n - 1
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[index] = nums1[m-1]
            m -= 1
        else:
            nums1[index] = nums2[n-1]
            n -= 1
        index -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge2(nums1, m, nums2, n))