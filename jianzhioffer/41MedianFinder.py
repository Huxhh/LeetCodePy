# coding=utf-8
# author huxh
# time 2020/3/30 5:36 PM

import heapq

class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []


    def addNum(self, num):
        if len(self.maxheap) == len(self.minheap):
            heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))
        else:
            heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))


    def findMedian(self):
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return self.minheap[0]