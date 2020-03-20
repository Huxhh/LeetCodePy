# coding=utf-8


def generateTheString(n):
    if n == 0:
        return ''

    res = ''
    if n % 2 == 1:
        res += 'a' * n
    else:
        res += 'a' * (n - 1)
        res += 'b'
    return res


def numTimesAllBlue(light):
    stat = [0] * len(light)

    maxs = 0
    res = []
    index = 0
    for k in light:
        stat[k - 1] = 1
        if k > maxs:
            maxs = k
        if k - 1 == index:
            index += 1
        while index < len(stat) and stat[index]:
            index += 1
        if index == maxs:
            res.append(k)

    return len(res)


def numOfMinutes(n, headID, manager, informTime):
    if n == 1:
        return informTime[headID]

    q = []
    for i in range(len(informTime)):
        if informTime[i] == 0:
            q.append(i)

    maxt = 0
    while q:
        index = q.pop(0)
        t = 0
        while index != -1:
            t += informTime[index]
            index = manager[index]
        maxt = max(t, maxt)

    return maxt


def frogPosition(n, edges, t, target):
    rd = [[0] * 110 for _ in range(110)]

    for i, j in edges:
        if i > j:
            i, j = j, i
        rd[i][j] = 1

    q = []
    q.append((1, 1, 0))
    while q:
        d, p, ct = q.pop(0)
        if ct == t:
            if d == target:
                return p

        if ct < t:
            if sum(rd[d]) == 0:
                q.append((d, p, ct + 1))
            for i in range(len(rd[d])):
                if rd[d][i] == 1:
                    q.append((i, p / sum(rd[d]), ct + 1))

    return 0


if __name__ == '__main__':
    # print(generateTheString(4)
    print(numTimesAllBlue([2,1,4,3,6,5]))
    # print(frogPosition(3, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
    # print(numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914]))