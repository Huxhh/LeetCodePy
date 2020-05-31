# coding=utf-8
# author huxh
# time 2020/3/21 9:34 AM


def canMeasureWater(x, y, z):
    s = []
    d = set()

    s.append((0, 0))
    while s:
        a, b = s.pop()
        if a == z or b == z or a + b == z:
            return True
        if (a, b) in d:
            continue
        d.add((a, b))
        s.append((a, 0))
        s.append((0, b))
        s.append((x, b))
        s.append((a, y))
        s.append((a - min(y - b, a), b + min(y - b, a)))
        s.append((a + min(x - a, b), b - min(x - a, b)))
    return False


def canMeasureWater2(x, y, z):
    import math
    if x + y < z:
        return False
    if x == 0 or y == 0:
        return z == 0 or x + y == z
    return z % math.gcd(x, y) == 0
