# coding=utf-8


def reverseWords(s):
    all_s = s.split(' ')
    all_s = all_s[::-1]
    all_s = [st for st in all_s if st]
    res = ' '.join([st for st in all_s])
    return res


if __name__ == '__main__':
    s = "a good   example"
    print(reverseWords(s))
