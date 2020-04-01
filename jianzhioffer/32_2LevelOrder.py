# coding=utf-8
# author huxh
# time 2020/3/27 3:42 PM


# O(N) O(N)
def levelOrder(root):
    res = []
    if not root:
        return res

    q = []
    q.append(root)
    while q:
        tmp = []
        for i in range(len(q)):
            r = q.pop(0)
            tmp.append(r.val)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        res.append(tmp)
    return res


# O(N) O(N)
def levelOrder2(root):
    res = {}

    def dfs(root, l):
        if not root:
            return

        if l not in res:
            res[l] = []
        res[l].append(root.val)
        dfs(root.left, l + 1)
        dfs(root.right, l + 1)

    dfs(root, 0)
    return [res[k] for k in res]
