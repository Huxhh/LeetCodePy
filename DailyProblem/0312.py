# coding=utf-8

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        l1 = len(str1)
        l2 = len(str2)
        l = min(l1, l2)
        for i in range(l, 0, -1):
            if l1 % i == 0 and l2 % i == 0:
                if self.check(str1[:i], str1) and self.check(str1[:i], str2):
                    return str1[:i]
        return ''

    def check(self, x, strc):
        n = int(len(strc) / len(x))
        s = ''
        for i in range(n):
            s += x
        return s == strc


class Solution2(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ''

        l1 = len(str1)
        l2 = len(str2)

        l = self.gcd(l1, l2)
        return str1[:l]

    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a % b)




if __name__ == '__main__':
    s = Solution2()
    print(s.gcdOfStrings('ABCABC', 'ABC'))