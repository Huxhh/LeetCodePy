# coding=utf-8
# author huxh
# time 2020/3/31 9:53 AM


def sortArray(nums):

    def qs(l, r):
        if l > r:
            return

        i = l
        j = r
        key = nums[l]
        while i < j:
            while i < j and nums[j] > key:
                j -= 1
            nums[i] = nums[j]

            while i < j and nums[i] <= key:
                i += 1
            nums[j] = nums[i]
        nums[j] = key
        qs(l, i - 1)
        qs(i + 1, r)
    qs(0, len(nums) - 1)
    return nums

import random
class Solution:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[r], nums[pivot] = nums[pivot], nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if l > r:
            return

        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


class Solution2:
    def merge_sort(self, nums, l, r):
        if l == r:
            return

        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i = l
        j = mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l:r + 1] = tmp[:]

    def sortArray(self, nums):
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


class Solution3:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if r >= heap_len or heap[l] > heap[r]:
                nex = l
            else:
                nex = r

            if heap[p] < heap[nex]:
                heap[nex], heap[p] = heap[p], heap[nex]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums):
        self.heap_sort(nums)
        return nums


