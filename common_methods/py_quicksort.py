# coding=utf-8

"""
快速排序的几种实现方法
"""


# 第一种，一行实现
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])


# 第二种，常见实现，两次循环
def quick_sort_double_loop(array, begin, end):
    if begin >= end:
        return

    i = begin
    j = end
    key = array[begin]

    while i < j:
        while i < j and array[j] > key:
            j -= 1
        array[i] = array[j]

        while i < j and array[i] <= key:
            i += 1
        array[j] = array[i]

    array[j] = key
    quick_sort_double_loop(array, begin, i - 1)
    quick_sort_double_loop(array, i + 1, end)


# 第三种，一次循环
class QS(object):
    def quick_sort(self, array, begin, end):
        if begin < end:
            mid = self.partition(array, begin, end)
            self.quick_sort(array, begin, mid - 1)
            self.quick_sort(array, mid + 1, end)

        return

    def partition(self, array, begin, end):
        x = array[end]
        i = begin - 1
        for j in range(begin, end):
            if array[j] < x:
                i += 1
                if i != j:
                    array[i], array[j] = array[j], array[i]

        i += 1
        array[i], array[end] = array[end], array[i]
        return i


# 第四种，用栈实现非递归的快排程序
def quick_sort_stack(array, begin, end):
    if begin >= end:
        return
    stack = []
    stack.append(begin)
    stack.append(end)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                if i != j:
                    array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


if __name__ == '__main__':
    a1 = [3, 2, 7, 4, 6, 0, 8]
    a2 = [3, 2, 7, 4, 6, 0, 8]
    a3 = [3, 2, 7, 4, 6, 0, 8]
    a4 = [3, 2, 7, 4, 6, 0, 8]
    q = QS()
    print(quick_sort(a1))
    quick_sort_double_loop(a2, 0, len(a2) - 1)
    print(a2)
    q.quick_sort(a3, 0, len(a3) - 1)
    print(a3)
    quick_sort_stack(a4, 0, len(a4) - 1)
    print(a4)
