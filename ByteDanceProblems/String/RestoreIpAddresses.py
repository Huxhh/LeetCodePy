# coding=utf-8

def restoreIpAddresses(s):
    res = []
    n = len(s)
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    if a + b + c + d == n:
                        A = int(s[0: a])
                        B = int(s[a: a + b])
                        C = int(s[a + b: a + b + c])
                        D = int(s[a + b + c:])
                        if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                            output = str(A) + '.' + str(B) + '.' + str(C) + '.' + str(D)
                            if len(output) == n + 3:
                                res.append(output)

    return res


class Solution:
    def restoreIpAddresses(self, s):
        res = []
        self.backtrack(s, 0, res, '')
        return res

    def backtrack(self, s, n, res, output):
        if n == 4:
            if not s:
                res.append(output)
                return
        else:
            for i in range(1, 4):
                if len(s) < i:
                    break
                val = int(s[0: i])
                if val <= 255 and len(str(val)) == i:
                    tmps = '.'
                    if n == 3:
                        tmps = ''
                    self.backtrack(s[i:], n + 1, res, output + s[0: i] +tmps)


if __name__ == '__main__':
    s1 = '25525519935'
    s = Solution()
    print(s.restoreIpAddresses(s1))
