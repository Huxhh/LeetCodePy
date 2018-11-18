# coding=utf-8

def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    imin = 0
    imax = m
    half_len = (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                med = nums2[j - 1]
            elif j == 0:
                med = nums1[i - 1]
            else:
                med = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return med
            if i == m:
                min_med = nums2[j]
            elif j == n:
                min_med = nums1[i]
            else:
                min_med = min(nums1[i], nums2[j])

            return (min_med + med) / 2


if __name__ == '__main__':
    print(findMedianSortedArrays([1,2], [3]))