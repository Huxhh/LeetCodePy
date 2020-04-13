# coding=utf-8
# author huxh
# time 2020/4/12 10:25 AM


def stringMatching(words):
    res = set()

    for s in words:
        for t in words:
            if s == t:
                continue
            if s in t:
                res.add(s)
    if not res:
        return []
    return list(res)


def processQueries(queries, m):
    res = []
    record = [0] * (m + 1)
    for i in range(1, m + 1):
        record[i] = i - 1

    moved = []

    for num in queries:
        if num in moved:
            tmp = 0
            for i in range(len(moved) - 1, -1, -1):
                if moved[i] == num:
                    if i < len(moved) - 1:
                        moved = moved[:i] + moved[i + 1:]
                    else:
                        moved.pop()
                    break
                tmp += 1
            res.append(tmp)
            moved.append(num)
        else:
            res.append(record[num])
            record[num] = 0
            moved.append(num)
            for i in range(1, num):
                record[i] += 1
    return res


def processQueries(queries, m):
    a = [i + 1 for i in range(m)]
    ans = []
    for q in queries:
        qi = a.index(q)
        ans.append(qi)
        a = [q] + a[: qi] + a[qi + 1:]
    return ans


def entityParser(text):
    if len(text) < 4:
        return text

    pat = {"quot":'"', "apos":'\'', "amp":'&', 'gt':'>', 'lt':'<', 'frasl':'/'}

    res = ''
    i = 0
    while i < len(text):
        if text[i] == '&':
            j = i + 1
            while j < len(text):
                if text[j] == ';':
                    break
                j += 1
            if text[j] != ';':
                continue
            content = text[i + 1:j]
            if content in pat:
                res += pat[content]
                i = j + 1
            else:
                res += text[i]
                i += 1
        else:
            res += text[i]
            i += 1
    return res





if __name__ == '__main__':
    # print(processQueries([10,7,3,3,9,4,1,4,9,9], 10))
    print(entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))