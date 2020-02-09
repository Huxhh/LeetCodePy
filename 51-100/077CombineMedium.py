# coding=utf-8

class Solution(object):
    def combine(self, n, k):
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        output = []
        backtrack()
        return output


if __name__ == '__main__':
    n = 4
    k = 2
    s = Solution()
    print(s.combine(n, k))