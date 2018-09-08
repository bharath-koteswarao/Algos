from bisect import bisect_left as bs


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 1
        self.isParent = True

    def __repr__(self):
        return str(self.val)


def find(x):
    if x.parent == x:
        return x
    else:
        return find(x.parent)


def merge(x, y):
    p1, p2 = find(x), find(y)
    if p1.val != p2.val:
        if p1.rank >= p2.rank:
            p2.parent = p1
            p1.rank += p2.rank
            p2.isParent = False
        else:
            p1.parent = p2
            p2.rank += p1.rank
            p1.isParent = False


if __name__ == '__main__':
    n, m, a, b = [int(__) for __ in input().strip().split()]
    dic = {i: Node(i) for i in range(1, n + 1)}
    for _ in range(m):
        p, q = [int(__) for __ in input().strip().split()]
        merge(dic[p], dic[q])
    conns = {}
    parent = {}
    for x in dic:
        p = find(dic[x]).val
        parent[x] = p
        if p in conns:
            conns[p].append(a * x)
            conns[p].append(b * x)
        else:
            conns[p] = [a * x, b * x]

