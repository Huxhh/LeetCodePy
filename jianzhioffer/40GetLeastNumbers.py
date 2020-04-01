# coding=utf-8
# author huxh
# time 2020/3/30 5:23 PM


def getLeastNumbers(arr, k):
    import heapq
    heap = []
    for n in arr:
        heapq.heappush(heap, -n)
        if len(heap) > k:
            heapq.heappop(heap)
    return [-x for x in heap]


def getLeastNumbers2(arr, k):
    if k == 0:
        return []

    if k == len(arr):
        return arr

    def qk(l, r):
        if l > r:
            return

        i = l
        j = r
        key = arr[l]
        while i < j:
            while i < j and arr[j] > key:
                j -= 1
            arr[i] = arr[j]

            while i < j and arr[i] <= key:
                i += 1
            arr[j] = arr[i]
        arr[i] = key
        if i == k:
            return arr[:k]
        elif i > k:
            return qk(l, i - 1)
        else:
            return qk(i + 1, r)
    return qk(0, len(arr) - 1)
