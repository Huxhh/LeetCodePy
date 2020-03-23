# coding=utf-8
# author huxh
# time 2020/3/20 11:46 AM

# 插入 O(1) O(n) 删除 O(n) O(n)
class CQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value):
        self.s1.append(value)


    def deleteHead(self):
        if self.s2:
            return self.s2.pop()
        if not self.s1:
            return -1
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()
