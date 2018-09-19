# coding=utf-8


"""
思路
方法1：使用数据结构栈，当碰到左括号时，将其入栈，碰到右括号时，将栈顶的元素出栈，应是能够配对，若不能则错误
        若最后栈中还有剩余元素，则也为错  时间复杂度O(n) 空间复杂度O(n)
"""


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