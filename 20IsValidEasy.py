# coding=utf-8


def isValid(s):
    left_dic = {'(': 1, '[': 2, '{': 3}
    right_dic = {')': 1, ']': 2, '}': 3}
    stack = []
    for i in range(0, len(s)):
        if s[i] in left_dic:
            stack.append(s[i])
        if s[i] in right_dic:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if left_dic[top] == right_dic[s[i]]:
                continue
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "([)]"
    print(isValid(s))