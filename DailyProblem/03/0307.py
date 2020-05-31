# coding=utf-8

from collections import deque

class MaxQueue(object):

    def __init__(self):
        self.q = deque()
        self.dq = deque()


    def max_value(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        return self.dq[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        while self.dq and self.dq[-1] < value:
            self.dq.pop()
        self.dq.append(value)
        self.q.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        ans = self.q.popleft()
        if ans == self.dq[0]:
            self.dq.popleft()
        return ans

