# coding=utf-8


"""
思路
方法一：暴力，检查每个子串是不是回文字符串
    时间复杂度 O(n^3) 空间复杂度 O(n^2)
方法二：从中心开始扩展，由于所含字母数有单数和偶数之分，所以有2n-1个中心
    时间复杂度O(n^2) 空间复杂度 O(1)
"""


class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if self.isPalindrome(substr):
                    if len(res) < len(substr):
                        res = substr[:]

        return res

    def isPalindrome(self, substr):
        n = len(substr)
        l = 0
        r = n - 1
        while l < r:
            if substr[l] != substr[r]:
                return False
            l += 1
            r -= 1

        return True




    def longestPalindrome2(self, s):
        if len(s) < 1:
            return ""
        start = 0
        end = 0
        n = len(s)
        for i in range(n):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]


    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
    

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


if __name__ == '__main__':
    solve = Solution()
    s = "cbbd"
    print(solve.longestPalindrome2(s))