# coding=utf-8
# author huxh
# time 2020/5/17 10:26 AM


# class Solution:
#     def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
#         res = 0
#         for i in range(len(startTime)):
#             if startTime[i] <= queryTime <= endTime[i]:
#                 res += 1
#         return res


def arrangeWords(text):
    words = text.split()
    words = [w.lower() for w in words]
    d = {}

    for w in words:
        if len(w) not in d:
            d[len(w)] = []
        d[len(w)].append(w)

    k = d.keys()
    k = sorted(k)
    res = []
    for s in k:
        res.extend(d[s])
    res[0] = res[0][0].upper() + res[0][1:]
    res = ' '.join(res)
    return res


def peopleIndexes(favoriteCompanies):
    favoriteCompanies = [sorted(x) for x in favoriteCompanies]

    res = []
    for i in range(len(favoriteCompanies)):
        ff = True
        for j in range(len(favoriteCompanies)):
            if i == j:
                continue
            flag = False
            if len(favoriteCompanies[i]) > len(favoriteCompanies[j]):
                flag = True
            else:
                for k in range(len(favoriteCompanies[i])):
                    if favoriteCompanies[i][k] in favoriteCompanies[j]:
                        continue
                    else:
                        flag = True
                        break
            ff &= flag
        if ff:
            res.append(i)
    return res


import math
class Solution:
    def numPoints(self, points, r: int) -> int:
        res = 0
        n = len(points)
        for i in range(n):
            for j in range(i, n):
                if self.dist(points[i], points[j]) > 2.0 * r + 1e-8:
                    continue
                center = self.get_circle_center(points[i], points[j], r)
                cnt = 0
                for k in range(n):
                    if self.dist(center, points[k]) < r + 1e-8:
                        cnt += 1
                res = max(res, cnt)
        return res

    def dist(self, a, b):
        return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))

    def get_circle_center(self, a, b, r):
        mid = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
        # angle = math.atan2(a[0] - b[0], a[1] - b[1])
        angle = math.atan((a[0] - b[0]) / (b[1] - a[1])) if b[1] - a[1] else math.pi / 2
        d = math.sqrt(r * r - math.pow(self.dist(a, mid), 2))
        return [mid[0] + d * math.cos(angle), mid[1] + d * math.sin(angle)]


if __name__ == '__main__':
    # print(peopleIndexes([["nxaqhyoprhlhvhyojanr","ovqdyfqmlpxapbjwtssm","qmsbphxzmnvflrwyvxlc","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"],["nxaqhyoprhlhvhyojanr","ovqdyfqmlpxapbjwtssm","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"],["ovqdyfqmlpxapbjwtssm","qmsbphxzmnvflrwyvxlc","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"]]))
    s = Solution()
    print(s.numPoints([[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], 5))