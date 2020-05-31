# coding=utf-8
# author huxh
# time 2020/3/27 9:56 AM


def hasGroupsSizeX(deck):
    from collections import Counter
    c = Counter(deck)
    import math
    from functools import reduce
    return reduce(math.gcd, c.values()) >= 2
