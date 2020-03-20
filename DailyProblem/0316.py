# coding=utf-8

def compressString(S):
    res = ''
    cnt = 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            cnt += 1
        else:
            res += S[i - 1] + str(cnt)
            cnt = 1
    res = res + S[-1] + str(cnt)
    if len(res) >= len(S):
        return S
    return res


if __name__ == '__main__':
    print(compressString('aabcccccaaa'))