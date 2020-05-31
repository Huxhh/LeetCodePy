# coding=utf-8
# author huxh
# time 2020/5/10 10:26 AM


def buildArray(target, n):
    if not target:
        return []
    res = []
    op = []
    index = 0
    for i in range(1, n + 1):
        if index == len(target):
            return op

        res.append(i)
        op.append('Push')
        if i != target[index]:
            op.append('Pop')
            res.pop()
        else:
            index += 1
    return op


def countTriplets(arr):
    mark = 0
    record = [0] * len(arr)
    for i in range(len(arr)):
        mark ^= arr[i]
        record[i] = mark
    res = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            for k in range(j, len(arr)):
                if i == 0:
                    tmp = 0
                else:
                    tmp = record[i - 1]
                if record[k] ^ record[j - 1] == record[j - 1] ^ tmp:
                    res += 1
    return res


def minTime(n, edges, hasApple):
    if n == 1:
        return 0

    s = set(hasApple)
    if len(s) == 1 and hasApple[0] == False:
        return 0

    d = {}
    for edge in edges:
        if edge[0] not in d:
            d[edge[0]] = []
        d[edge[0]].append(edge[1])

    cnt = 0
    for h in hasApple:
        if h:
            cnt += 1

    def dfs(cur, time, curcnt):
        if hasApple[cur]:
            curcnt += 1

        if cur not in d:
            return curcnt, time + 1

        total_time = 0
        total = 0
        for child in d[cur]:
            ct, aftime = dfs(child, time + 1, curcnt)
            if ct > curcnt:
                total += (ct - curcnt)
                total_time += (aftime - time)

        return curcnt + total, time + total_time + 1

    _, t = dfs(0, 0, 0)

    return t - 1


def ways(pizza, k):
    if k == 1:
        return 1





if __name__ == '__main__':
    # print(buildArray([1, 2], 4))
    # print(countTriplets([7,11,12,9,5,2,7,17,22]))
    print(minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [0,0,1,0,0,1,0]))