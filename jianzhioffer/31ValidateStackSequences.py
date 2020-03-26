# coding=utf-8
# author huxh
# time 2020/3/26 10:50 AM


# O(N) O(N)
def validateStackSequences(pushed, popped):
    s = []
    index = 0
    for n in pushed:
        s.append(n)
        while s and s[-1] == popped[index]:
            index += 1
            s.pop()
    if s:
        return False
    return True
