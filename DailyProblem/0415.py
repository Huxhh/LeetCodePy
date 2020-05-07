# coding=utf-8
# author huxh
# time 2020/4/15 12:07 AM


def updateMatrix2(matrix):
    import collections
    m, n = len(matrix), len(matrix[0])
    dist = [[0] * n for _ in range(m)]
    zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
    q = collections.deque(zeroes_pos)
    seen = set(zeroes_pos)

    while q:
        i, j = q.popleft()
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
                seen.add((ni, nj))

    return dist


if __name__ == '__main__':
    print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
