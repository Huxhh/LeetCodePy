# coding=utf-8
# author huxh
# time 2020/3/27 4:57 PM


# O(N) O(N)
def pathSum(root, sum):
    if not root:
        return []

    res = []

    def back(r, path, s):
        if not r:
            return

        s += r.val
        path.append(r.val)
        if not r.left and not r.right and s == sum:
            res.append(path[:])
            path.pop()
            return

        back(r.left, path, s)
        back(r.right, path, s)
        path.pop()

    back(root, [], 0)
    return res
