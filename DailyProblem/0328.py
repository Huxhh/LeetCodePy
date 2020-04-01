# coding=utf-8
# author huxh
# time 2020/3/28 10:02 AM
import collections
from functools import reduce


def minimumLengthEncoding(words):
    all_words = set(words)
    for w in words:
        for i in range(1, len(w)):
            all_words.discard(w[i:])
    return sum([len(w) + 1 for w in all_words])


def minimumLengthEncoding2(words):
    words = list(set(words))  # remove duplicates
    # Trie is a nested dictionary with nodes created
    # when fetched entries are missing
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()

    # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
    nodes = [reduce(dict.__getitem__, word[::-1], trie)
             for word in words]

    # Add word to the answer if it's node has no neighbors
    return sum(len(word) + 1
               for i, word in enumerate(words)
               if len(nodes[i]) == 0)


def minimumLengthEncoding3(words):
    N = len(words)
    # 逆序字典序排序
    words.sort(key=lambda word: word[::-1])

    res = 0
    for i in range(N):
        if i + 1 < N and words[i + 1].endswith(words[i]):
            # 当前单词是下一个单词的后缀，丢弃
            pass
        else:
            res += len(words[i]) + 1  # 单词加上一个 '#' 的长度

    return res

