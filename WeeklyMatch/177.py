# coding=utf-8

def daysBetweenDates(date1, date2):
    import time
    if date1 == date2:
        return 0

    date1 += ' 00:00:00'
    date2 += ' 00:00:00'

    timearray1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
    timearray2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
    timesp1 = time.mktime(timearray1)
    timesp2 = time.mktime(timearray2)
    res = abs(timesp2 - timesp1) // (24 * 60 * 60)

    return int(res)


def validateBinaryTreeNodes(n, leftChild, rightChild):
    if n == 1:
        return True

    que = []
    que.append(0)
    visited = [0] * n
    while que:
        root = que.pop(0)
        if visited[root]:
            return False
        visited[root] = 1
        if leftChild[root] != -1:
            que.append(leftChild[root])
        if rightChild[root] != -1:
            que.append(rightChild[root])

    if sum(visited) != n:
        return False

    return True


def closestDivisors(num):
    import math
    num1 = num + 1
    num2 = num + 2
    res1 = []
    res2 = []
    for i in range(1, int(math.sqrt(num1) + 1)):
        if num1 % i == 0:
            res1.append((i, int(num1 / i)))
    for i in range(1, int(math.sqrt(num2) + 1)):
        if num2 % i == 0:
            res2.append((i, int(num2 / i)))

    mins = 100000000000
    for a,b in res1:
        if abs(a - b) < mins:
            ans = [a,b]
            mins = abs(a - b)
    for a,b in res2:
        if abs(a - b) < mins:
            ans = [a,b]
            mins = abs(a - b)
    return ans


def largestMultipleOfThree(digits):
    if not digits:
        return ''

    digits = sorted(digits, reverse=True)
    flag = 1
    s = sum(digits)

    if s % 3 == 1:
        flag = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 3 == 1:
                digits.remove(digits[i])
                flag = 1
                break
        if not flag:
            tmp = 0
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] % 3 == 2:
                    digits.remove(digits[i])
                    tmp += 1
                    if tmp == 2:
                        flag = 1
                        break

    elif s % 3 == 2:
        flag = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 3 == 2:
                digits.remove(digits[i])
                flag = 1
                break
        if not flag:
            tmp = 0
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] % 3 == 1:
                    digits.remove(digits[i])
                    tmp += 1
                    if tmp == 2:
                        flag = 1
                        break

    ans = ''
    if not digits:
        return ''
    if not flag:
        return ''
    while digits:
        ans += str(digits.pop(0))
        if ans == '0':
            ans = ''
    if ans == '':
        ans = '0'
    return ans



if __name__ == '__main__':
    # date1 = '2020-01-15'
    # date2 = '2019-12-31'
    # print(daysBetweenDates(date1, date2))
    leftchild = [-1,2,1]
    rightchild = [-1,-1,-1]
    print(validateBinaryTreeNodes(5, leftchild, rightchild))
    # print(closestDivisors(944361386))
    # print(largestMultipleOfThree([8,7,6,1,0]))
