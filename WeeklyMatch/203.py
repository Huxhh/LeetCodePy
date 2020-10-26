# coding=utf-8
# author huxh
# time 2020/8/28 9:18 PM

def mostVisited(n, rounds):
    res = []
    count = [0] * n
    cur = rounds[0] - 1
    for i in range(1, len(rounds)):
        while cur + 1 != rounds[i]:
            count[cur] += 1
            cur = (cur + 1) % n
    count[cur] += 1
    maxs = max(count)
    print(count)
    for i in range(len(count)):
        if count[i] == maxs:
            res.append(i + 1)
    return sorted(res)


def maxCoins(piles):
    piles = sorted(piles)
    l = 0
    r = len(piles) - 2
    res = 0
    while l < r:
        res += piles[r]
        l += 1
        r -= 2
    return res


if __name__ == '__main__':
    print(mostVisited(2, [2,1,2,1,2,1,2,1,2]))