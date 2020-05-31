# coding=utf-8

class Solution(object):
    def merge(self, A, m, B, n):
        if n == 0:
            return
        if m == 0:
            A[:] = B[:]
            return


        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if A[m] >= B[n]:
                A[n + m + 1] = A[m]
                m -= 1
            else:
                A[n + m + 1] = B[n]
                n -= 1

        if n >= 0:
            A[:n + 1] = B[:n + 1]
        return A


if __name__ == '__main__':
    s = Solution()
    print(s.merge([0], 0, [1], 1))
