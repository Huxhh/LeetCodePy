# coding=utf-8
# author huxh
# time 2020/5/15 4:24 PM


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map={0:1}
        ans=0
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum-k in map:
                ans=ans+map[sum-k]
            if sum in map:
                map[sum]=map[sum]+1
            else:map[sum]=1
        return ans
