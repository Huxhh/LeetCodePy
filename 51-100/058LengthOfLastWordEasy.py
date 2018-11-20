# coding=utf-8

"""
思路
思路常规，注意尾部空格即可
"""

def lengthOfLastWord(s):
    s = s.rstrip()
    l = s.split(' ')
    if not l[-1]:
        if len(l) == 1:
            return 0
        else:
            return len(l[-2])
    else:
        return len(l[-1])



if __name__ == '__main__':
    print(lengthOfLastWord("b a "))