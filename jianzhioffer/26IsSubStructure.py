# coding=utf-8
# author huxh
# time 2020/3/25 10:22 AM


# O(MN) O(M)
class Solution:
    def isSubStructure(self, A, B):
        if not A or not B:
            return False

        return self.back(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def back(self, a, b):
        if not b:
            return True

        if not a or a.val != b.val:
            return False

        return self.back(a.left, b.left) and self.back(a.right, b.right)
