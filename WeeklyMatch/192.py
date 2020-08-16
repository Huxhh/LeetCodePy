# coding=utf-8
# author huxh
# time 2020/6/7 10:06 AM


def shuffle(nums, n):
    res = []
    a = nums[:n]
    b = nums[n:]
    for x, y in zip(a, b):
        res.extend([x, y])
    return res


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        mid = arr[(len(arr) - 1 ) // 2]

        res = []
        i = 0
        j = len(arr) - 1
        while i <= j and len(res) < k:
            if abs(arr[i] - mid) > abs(arr[j] - mid):
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
        return res


from collections import deque
class BrowserHistory:

    def __init__(self, homepage: str):
        self.fwd = deque()
        self.bwd = deque()
        self.cur = homepage

    def visit(self, url: str) -> None:
        self.fwd = deque()
        self.bwd.append(self.cur)
        self.cur = url

    def back(self, steps: int) -> str:
        if not self.bwd:
            return self.cur
        self.fwd.appendleft(self.cur)
        steps = min(steps, len(self.bwd))
        while steps - 1:
            self.fwd.appendleft(self.bwd.pop())
            steps -= 1
        self.cur = self.bwd.pop()
        return self.cur

    def forward(self, steps: int) -> str:
        if not self.fwd:
            return self.cur
        self.bwd.append(self.cur)
        steps = min(steps, len(self.fwd))
        while steps - 1:
            self.bwd.append(self.fwd.popleft())
            steps -= 1
        self.cur = self.fwd.popleft()
        return self.cur

