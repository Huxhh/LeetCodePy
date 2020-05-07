# coding=utf-8
# author huxh
# time 2020/4/19 10:30 AM


def reformat(s):
    char = []
    digits = []
    for c in s:
        if '0' <= c <= '9':
            digits.append(c)
        else:
            char.append(c)

    if abs(len(char) - len(digits)) >= 2:
        return ''

    res = ''
    if len(char) > len(digits):
        for i in range(len(digits)):
            res += char[i]
            res += digits[i]
        res += char[-1]
    elif len(char) < len(digits):
        for i in range(len(char)):
            res += digits[i]
            res += char[i]
        res += digits[-1]
    else:
        for i in range(len(char)):
            res += digits[i]
            res += char[i]
    return res


class Solution:
    def displayTable(self, orders):
        d = {}
        dish = set()
        for order in orders:
            if order[1] not in d:
                d[order[1]] = []
            d[order[1]].append(order[2])
            dish.add(order[2])

        dish = sorted(dish)
        res = [['Table']]
        for di in dish:
            res[0].append(di)

        keys = sorted(d.keys(), key=lambda x: int(x))
        for k in keys:
            tmp = [k]
            for di in dish:
                if di not in d[k]:
                    tmp.append('0')
                else:
                    cnt = 0
                    for o in d[k]:
                        if o == di:
                            cnt += 1
                    tmp.append(str(cnt))
            res.append(tmp)
        return res


def minNumberOfFrogs(croakOfFrogs):
    from collections import Counter
    c = Counter(croakOfFrogs)

    if not c['a'] == c['r'] == c['c'] == c['o'] == c['k']:
        return -1

    chars = ['c', 'r', 'o', 'a', 'k']
    dic = {}
    for char in chars:
        dic[char] = 0

    res = 0
    tmp = 0
    for d in croakOfFrogs:
        dic[d] += 1
        for i in range(len(chars) - 1, 0, -1):
            for j in range(i):
                if dic[chars[i]] > dic[chars[j]]:
                    return -1

        if d == 'c':
            tmp += 1
        if d == 'k':
            res = max(res, tmp)
            tmp -= 1
    return res


class Solution2:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        from itertools import combinations
        if m < k:
            return 0

        mod = 1000000007
        res = 0
        for i in range(k, m + 1):
            tmp = n - k
            after = 1
            while tmp:
                after *= i
                tmp -= 1
            res += len(list(combinations([x for x in range(1, i)], k - 1))) * after
            res %= mod
        return res



if __name__ == '__main__':
    # s = Solution()
    # print(s.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
    # print(minNumberOfFrogs("aoocrrackk"))
    s = Solution2()
    print(s.numOfArrays(37,17,7))