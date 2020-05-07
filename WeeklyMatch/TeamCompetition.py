# coding=utf-8
# author huxh
# time 2020/4/25 2:56 PM




def minTime(time, m):
    if m >= len(time):
        return 0

    l = 0
    r = 0
    for t in time:
        # if t > l:
        #     l = t
        r += t

    while l < r:
        mid = (l + r) // 2
        u = 1
        s = 0
        maxs = time[0]
        for i in range(len(time)):
            maxs = max(maxs, time[i])
            s += time[i]
            if s - maxs > mid:
                u += 1
                s = time[i]
                maxs = time[i]

        if u <= m:
            r = mid
        else:
            l = mid + 1
    return r


if __name__ == '__main__':
    print(minTime([1,2,3,3], 2))