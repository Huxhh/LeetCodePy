# coding=utf-8


def countCharacters(words, chars):

    from collections import Counter
    if not words or not chars:
        return 0

    res = 0
    c = Counter(chars)
    for w in words:
        flag = 1
        c1 = Counter(w)
        for a in c1:
            if c1[a] > c[a]:
                flag = 0
                break
        if flag:
            res += len(w)
    return res