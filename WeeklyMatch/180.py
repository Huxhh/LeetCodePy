# coding=utf-8

def luckyNumbers(matrix):
    if not matrix:
        return []

    mins = [min(matrix[i]) for i in range(len(matrix))]
    maxs = []
    for j in range(len(matrix[0])):
        m = 0
        for i in range(len(matrix)):
            m = max(m, matrix[i][j])
        maxs.append(m)

    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == mins[i] and matrix[i][j] == maxs[j]:
                res.append(matrix[i][j])
    return res


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = [-1] * maxSize
        self.index = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.index != len(self.stack):
            self.stack[self.index] = x
            self.index += 1


    def pop(self):
        """
        :rtype: int
        """
        if self.index == 0:
            return -1
        else:
            ans = self.stack[self.index - 1]
            self.index -= 1
            return ans

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(k):
            if i >= self.index:
                break
            self.stack[i] += val


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def balanceBST(root):
    if not root:
        return root

    nums = []

    def inorder(r):
        if not r:
            return

        inorder(r.left)
        nums.append(r.val)
        inorder(r.right)

    inorder(root)

    def buildtree(r, cnode):
        tmp = r
        while tmp:
            if cnode.val < tmp.val:
                if not tmp.left:
                    tmp.left = cnode
                    return
                else:
                    tmp = tmp.left
            else:
                if not tmp.right:
                    tmp.right = cnode
                    return
                else:
                    tmp = tmp.right

    newnums = []

    def reorder(l, r):
        if l > r:
            return

        mid = (l + r) // 2
        newnums.append(nums[mid])
        reorder(l, mid - 1)
        reorder(mid + 1, r)

    reorder(0, len(nums) - 1)

    newRoot = TreeNode(newnums[0])
    for i in range(1, len(newnums)):
        tnode = TreeNode(newnums[i])
        buildtree(newRoot, tnode)
    return newRoot


def balanceBST2(root):
    if not root:
        return root

    nums = []

    def inorder(r):
        if not r:
            return r

        inorder(r.left)
        nums.append(r.val)
        inorder(r.right)

    inorder(root)

    def build(l, r):
        if l > r:
            return

        mid = (l + r) // 2
        newNode = TreeNode(nums[mid])
        newNode.left = build(l, mid - 1)
        newNode.right = build(mid + 1, r)
        return newNode

    return build(0, len(nums) - 1)


def maxPerformance(n, speed, efficiency, k):
    m = 1e9 + 7

    import heapq

    es = []
    for i in range(n):
        es.append((efficiency[i], speed[i]))

    es.sort(reverse=True)
    print(es)
    heap = []
    ans = 0
    s = 0
    for i in range(n):
        heapq.heappush(heap, es[i][1])
        s += es[i][1]
        if len(heap) > k:
            tmp = heapq.heappop(heap)
            s -= tmp
        ans = max(ans, s * es[i][0])
    return int(ans % m)


if __name__ == '__main__':
    # m = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    # print(luckyNumbers(m))
    n = 6
    speed = [5, 4, 3, 7, 6, 2]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 3
    print(maxPerformance(n, speed, efficiency, k))