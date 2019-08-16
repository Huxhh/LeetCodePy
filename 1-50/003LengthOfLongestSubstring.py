# coding=utf-8

"""
思路
找出最长的不含重复字符的子串
方法1：暴力查找，在每一个子串当中查找是否含有重复字符 时间复杂度O(n^3) 空间复杂度O(min(n,m))
方法2：滑动窗口，相当于左侧固定，右侧向后滑动，如果没有重复字符就持续滑动，有则停下
时间复杂度O(n) 空间复杂度O(min(n,m))
方法3：优化的滑动窗口，创建字符到索引的映射，使用索引直接计算
时间复杂度O(n) 空间复杂度O(min(m, n))
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                if self.isUnique(i, j, s):
                    ans = max(j - i, ans)

        return ans

    def isUnique(self, i, j, s):
        chars = []
        for k in range(i, j):
            ch = s[k]
            if ch in chars:
                return False
            chars.append(ch)

        return True


def lengthOfLongestSubstring2(s):
    n = len(s)
    ans = 0
    res = []
    i, j = 0, 0
    while i < n and j < n:
        if s[j] not in res:
            res.append(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            res.remove(s[i])
            i += 1
    return ans


def lengthOfLongestSubstring3(s):
    n = len(s)
    ans = 0
    d = {}
    i = 0
    for j in range(n):
        if s[j] in d.keys():
            i = max(d[s[j]], i)
        d[s[j]] = j + 1
        ans = max(ans, j - i + 1)
    return ans


if __name__ == '__main__':
    s ="pwwkew"
    # so = Solution()
    print(lengthOfLongestSubstring3(s))