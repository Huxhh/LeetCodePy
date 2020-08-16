# coding=utf-8
# author huxh
# time 2020/7/9 10:55 PM


class Trie:
    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        curnode = self.root
        for c in word[::-1]:
            if c not in curnode:
                curnode[c] = {}
            curnode = curnode[c]
        curnode[self.end] = True


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        dp = [-1e9] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            curpos = trie.root
            for j in range(i, 0, -1):
                c = sentence[j - 1]
                if c not in curpos:
                    break
                elif -1 in curpos[c]:
                    dp[i] = min(dp[i], dp[j - 1])

                if dp[i] == 0:
                    break
                curpos = curpos[c]
        return dp[n]




