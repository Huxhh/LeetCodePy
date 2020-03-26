# coding=utf-8
# author huxh
# time 2020/3/26 10:46 AM


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mis = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if not self.mis:
            self.mis.append(x)
        else:
            if x < self.mis[-1]:
                self.mis.append(x)
            else:
                self.mis.append(self.mis[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.mis.pop()
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.mis[-1]

