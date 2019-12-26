# coding=utf-8


def findSubstring(s, words):
    if not s or not words:
        return []

    ans = []

    one_word = len(words[0])
    all_len = len(words) * one_word

    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    for i in range(0, len(s) - all_len + 1):
        tmp = s[i:i + all_len]
        tmp_word = {}
        for j in range(0, all_len, one_word):
            if tmp[j:j + one_word] not in tmp_word:
                tmp_word[tmp[j:j + one_word]] = 1
            else:
                tmp_word[tmp[j:j + one_word]] += 1
        if tmp_word == word_count:
            ans.append(i)
    return ans


def findSubString2(s, words):
    from collections import Counter
    if not s or not words:
        return []

    res = []

    one_word = len(words[0])
    word_num = len(words)
    n = len(s)
    cwords = Counter(words)

    for i in range(0, one_word):
        left = i
        right = i
        current_num = 0
        counter = Counter()
        while right + one_word <= n:
            now_word = s[right:right + one_word]
            right += one_word
            counter[now_word] += 1
            current_num += 1
            while counter[now_word] > cwords[now_word]:
                left_word = s[left:left + one_word]
                left += one_word
                counter[left_word] -= 1
                current_num -=1
            if current_num == word_num:
                res.append(left)
    return res


def findSubString3(s, words):
    from collections import Counter
    if not s or not words:
        return []

    res = []

    one_word = len(words[0])
    word_num = len(words)
    n = len(s)
    if n < one_word: return []
    cwords = Counter(words)

    for i in range(0, one_word):
        left = i
        right = i
        current_num = 0
        counter = Counter()
        while right + one_word <= n:
            now_word = s[right:right + one_word]
            right += one_word
            if now_word not in words:
                counter.clear()
                current_num = 0
                left = right
            else:
                counter[now_word] += 1
                current_num += 1
            while counter[now_word] > cwords[now_word]:
                left_word = s[left:left + one_word]
                left += one_word
                counter[left_word] -= 1
                current_num -=1
            if current_num == word_num:
                res.append(left)
    return res

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(findSubstring(s, words))
