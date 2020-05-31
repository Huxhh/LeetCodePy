# coding=utf-8
# author huxh
# time 2020/5/9 11:05 AM


def oneEditAway(first, second):
    l1 = len(first)
    l2 = len(second)
    if abs(l1 - l2) > 1:
        return False
    i, j = 0, 0
    flag = True
    while i < l1 and j < l2:
        if first[i] != second[j]:
            if not flag:
                return False
            flag = False
            if l1 > l2:
                j -= 1
            if l2 > l1:
                i -= 1
        i += 1
        j += 1
    return True

if __name__ == '__main__':
    print(oneEditAway('abc', 'bbcc'))