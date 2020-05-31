# coding=utf-8
# author huxh
# time 2020/5/24 10:11 AM

def isPrefixOfWord(sentence, searchWord):
    if not sentence:
        return -1

    res = -1
    words = sentence.split(' ')
    for i in range(len(words)):
        if len(searchWord) > len(words[i]):
            continue
        else:
            if words[i][:len(searchWord)] == searchWord:
                if res == -1:
                    res = i + 1
    return res

def maxVowels(s, k):
    l = 0
    r = k - 1
    res = 0
    chars = ['a', 'e', 'i', 'o', 'u']
    for i in range(k):
        if s[i] in chars:
            res += 1
    ans = res
    l += 1
    r += 1
    while r < len(s):
        if s[l - 1] in chars:
            res -= 1
        if s[r] in chars:
            res += 1
        ans = max(ans, res)
        l += 1
        r += 1
    return ans

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        total_seq = []

        def dfs(cur, path):
            if not cur:
                return

            path.append(cur.val)
            if not cur.left and not cur.right:
                total_seq.append(path[:])

            if cur.left:
                dfs(cur.left, path)
            if cur.right:
                dfs(cur.right, path)

            path.pop()
            return

        dfs(root, [])
        print(total_seq)
        res = 0
        for seq in total_seq:
            if self.check(seq):
                res += 1
        return res

    def check(self, seq):
        c = Counter(seq)
        flag = True
        for k in c:
            if c[k] & 1:
                if flag:
                    flag = False
                else:
                    return False
        return True


def maxDotProduct(nums1, nums2):
    if max(nums2) < 0 < min(nums1):
        return min(nums1) * max(nums2)

    if max(nums1) < 0 < min(nums2):
        return min(nums2) * max(nums1)

    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

    ans = 0
    rows = len(nums1)
    cols = len(nums2)
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            res = nums1[i - 1] * nums2[j - 1]
            dp[i][j] = max(dp[i - 1][j - 1] + res, dp[i - 1][j], dp[i][j - 1])
            ans = max(ans, dp[i][j])
    return ans


if __name__ == '__main__':
    # root = TreeNode(2)
    # root.left = TreeNode(1)
    # root.left.left = TreeNode(1)
    # s = Solution()
    # print(s.pseudoPalindromicPaths(root))
    print(maxDotProduct([5,-4,-3],[-4,-3,0,-4,2]))
