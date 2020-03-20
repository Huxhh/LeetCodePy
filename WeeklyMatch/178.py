# coding=utf-8

def smallerNumbersThanCurrent(nums):
    if not nums:
        return []

    res = []
    for num in nums:
        tmp = 0
        for n in nums:
            if n < num:
                tmp += 1
        res.append(tmp)

    return res


def rankTeams(votes):
    if len(votes) == 1:
        return votes[0]

    d = {}
    for c in votes:
        for i in range(len(c)):
            if c[i] not in d:
                d[c[i]] = [0] * len(c)
            d[c[i]][i] += 1

    dic = sorted(d.items())
    dic = sorted(dic, key=lambda x:x[1], reverse=True)
    res = [r[0] for r in dic]

    return ''.join(res)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubPath(self, head, root):
        q = []
        q.append(root)
        while q:
            r = q.pop(0)
            if r.right:
                q.append(r.right)
            if r.left:
                q.append(r.left)

            if head.val == r.val:
                res = self.isTrue(head, r)
                if res:
                    return True
        return False

    def isTrue(self, head, root):
        if not root:
            return False

        if head.val != root.val:
            return False

        if head.next:
            head = head.next
        else:
            return True

        return self.isTrue(head, root.left) or self.isTrue(head, root.right)


if __name__ == '__main__':
    # print(smallerNumbersThanCurrent([7,7,7,7]))
    votes = ["WXYZ","XYZW"]
    print(rankTeams(votes))
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # head = ListNode(1)
    # head.next = ListNode(2)
    # s = Solution()
    # print(s.isSubPath(head, root))
