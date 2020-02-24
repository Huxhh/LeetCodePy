# coding=utf-8


def checkIfExist(arr):
    if not arr:
        return False

    have_0 = False
    arr.sort()
    for i in arr:
        if i != 0:
            if 2 * i in arr:
                return True
        else:
            if not have_0:
                have_0 = True
            else:
                return True
    return False


def minSteps(s, t):
    d = {}
    for w in t:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1

    for w in s:
        if w in d and d[w] != 0:
            d[w] -= 1

    res = 0
    for k in d:
        res += d[k]

    return res


class TweetCounts(object):

    def __init__(self):
        self.record = {}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        if tweetName in self.record:
            self.record[tweetName].append(time)
        else:
            self.record[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        if tweetName not in self.record:
            return None

        res = []
        fq = 0
        if freq == 'minute':
            fq = 60
        if freq == 'hour':
            fq = 3600
        if freq == 'day':
            fq = 3600 * 24

        tmp = {}
        for t in self.record[tweetName]:
            if startTime <= t < endTime:
                if (t - startTime) // fq in tmp:
                    tmp[(t - startTime) // fq] += 1
                else:
                    tmp[(t - startTime) // fq] = 1

        n = (endTime - startTime) // fq + 1
        for i in range(n):
            if i in tmp:
                res.append(tmp[i])
            else:
                res.append(0)
        return res


def maxStudents(seats):
    if not seats:
        return 0

    m = len(seats)
    n = len(seats[0])
    dr = [0, -1, -1, -1, 0]
    dc = [-1, -1, 0, 1, 1]
    for i in range(m):
        for j in range(n):
            if seats[i][j] == '.':
                flag = 1
                for k in range(len(dr)):
                    tr = i + dr[k]
                    tc = j + dc[k]
                    if 0 <= tr < m and 0 <= tc < n:
                        if seats[tr][tc] == '1':
                            flag = 0
                if flag:
                    seats[i][j] = '1'

    res = 0

    for i in range(m):
        for j in range(n):
            if seats[i][j] == '1':
                res += 1
    return res



if __name__ == '__main__':
    # arr = [10,2,3,5]
    # print(checkIfExist(arr))
    s = "aaabb"
    t = "aaccc"
    print(minSteps(s, t))

    # seats = [["#",".",".",".","#"],
    #           [".","#",".","#","."],
    #           [".",".","#",".","."],
    #           [".","#",".","#","."],
    #           ["#",".",".",".","#"]]
    # print(maxStudents(seats))
