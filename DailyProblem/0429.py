# coding=utf-8
# author huxh
# time 2020/4/29 5:35 PM


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l = 0
        r = mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        index = self.bs(0, peak, target, mountain_arr)
        if index != -1:
            return index
        index = self.bs(peak, mountain_arr.length() - 1, target, mountain_arr, key=lambda x: -x)
        return index

    def bs(self, l, r, target, mountain_arr, key=lambda x: x):
        target = key(target)
        while l <= r:
            mid = (l + r) // 2
            cur = key(mountain_arr.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
