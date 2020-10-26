# coding=utf-8
# author huxh
# time 2020/8/17 12:15 AM


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        lh = 0
        rh = 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lh:
                    lh = height[l]
                else:
                    res += (lh - height[l])
                l += 1
            else:
                if height[r] >= rh:
                    rh = height[r]
                else:
                    res += (rh - height[r])
                r -= 1
        return res
