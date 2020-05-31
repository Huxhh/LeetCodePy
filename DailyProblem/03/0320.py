# coding=utf-8
# author huxh
# time 2020/3/20 10:02 AM


def getLeastNumbers(arr, k):
    import heapq
    h = []
    for n in arr:
        heapq.heappush(h, -n)
        if len(h) > k:
            heapq.heappop(h)
    h = [-x for x in h]
    return h


def getLeastNumbers2(arr, k):
    if k == 0:
        return []
    if k == len(arr):
        return arr

    def qs(begin, end, arr, k):
        if begin > end:
            return

        i = begin
        j = end
        key = arr[begin]
        while i < j:
            while i < j and arr[j] > key:
                j -= 1
            arr[i] = arr[j]

            while i < j and arr[i] <= key:
                i += 1
            arr[j] = arr[i]
        arr[j] = key
        if i == k:
            return arr[:k]
        if i > k:
            return qs(begin, i - 1, arr, k)
        else:
            return qs(i + 1, end, arr, k)

    return qs(0, len(arr) - 1, arr, k)


if __name__ == '__main__':
    print(getLeastNumbers2([0,0,2,3,2,1,1,2,0,4], 10))
