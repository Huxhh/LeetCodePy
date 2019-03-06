# coding=utf-8


class Solution:
    def checkInclusion(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False

        list1 = [0] * 26
        list2 = [0] * 26
        for i in range(l1):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1

        for i in range(l2 - l1):
            if self.equal(list1, list2):
                return True
            list2[ord(s2[i + l1]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] -= 1

        return self.equal(list1, list2)

    def equal(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    s1 = 'ab'
    s2 = 'eidbaooo'
    print(s.checkInclusion(s1, s2))
