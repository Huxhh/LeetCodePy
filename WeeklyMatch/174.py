# coding=utf-8

def kWeakestRows(mat, k):
    if not mat:
        return []

    d = {}
    for i in range(len(mat)):
        s = sum(mat[i])
        d[i] = s

    list1 = sorted(d.items(), key=lambda x: x[1])
    res = list1[:k]
    ret = []
    for r in res:
        ret.append(r[0])
    return ret


def minSetSize(arr):
    from collections import Counter

    if not arr:
        return []

    c = Counter(arr)

    n = len(arr)
    num = 0
    t = 0
    for k, v in c.most_common(n):
        if t >= n // 2:
            break
        t += v
        num += 1

    return num


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxProduct(self, root):
        mod = 10**9 + 7
        s = 0
        s = self.allSum(root, s)
        self.maxs = 0
        self.subtreeSum(root, s)
        return self.maxs % mod

    def allSum(self, root, s):
        s += root.val
        if root.left:
            s = self.allSum(root.left, s)
        if root.right:
            s = self.allSum(root.right, s)
        return s

    def subtreeSum(self, root, ts):
        if not root:
            return 0
        s = root.val + self.subtreeSum(root.left, ts) + self.subtreeSum(root.right, ts)
        self.maxs = max(self.maxs, s * (ts - s))
        return s


if __name__ == '__main__':
 #    mat =  [[1,1,0,0,0],
 # [1,1,1,1,0],
 # [1,0,0,0,0],
 # [1,1,0,0,0],
 # [1,1,1,1,1]]
 #    k = 3
 #    print(kWeakestRows(mat, k))

    # arr = [3,3,3,3,5,5,5,2,2,7]
#     # print(minSetSize(arr))

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    s = Solution()
    print(s.maxProduct(root))