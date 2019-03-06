# coding=utf-8


def lengthOfLongestSubstring(s):
    maxLength = 0
    currentLength = 0

    usedChar = {}

    for index, char in enumerate(s):
        if char in usedChar and currentLength <= usedChar[char]:
            currentLength = usedChar[char] + 1
        else:
            maxLength = max(maxLength, index - currentLength + 1)
        usedChar[char] = index


    return maxLength


def lengthOfLongestSubstring2(s):
    maxLength = 0
    currentLength = 0
    position = {}
    for i in range(len(s)):
        pre_index = -1
        if s[i] in position:
            pre_index = position[s[i]]

        if pre_index < 0 or currentLength < i - pre_index:
            currentLength += 1
        else:
            maxLength = max(maxLength, currentLength)

            currentLength = i - pre_index

        position[s[i]] = i

    maxLength = max(maxLength, currentLength)

    return maxLength



if __name__ == '__main__':
    s = 'pwwkew'
    print(lengthOfLongestSubstring2(s))
