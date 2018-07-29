class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 1
        self.isParent = True


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


def c(n, r):
    if n < r:
        return 0
    elif n == r:
        return 1
    else:
        numerator = 1
        denominator = 1
        for j in range(n, n - r, -1):
            numerator *= j
        # print("numerator is ",numerator)
        for j in range(r, 0, -1):
            denominator *= j
        # print("denominator is ",denominator)
        return numerator / denominator


if __name__ == '__main__':
    n, q = [int(__) for __ in input().strip().split()]
    dic = {}
    for i in range(n):
        dic[i] = Node(i)
    for _ in range(q):
        a, b = [int(__) for __ in input().strip().split()]
        merge(dic[a], dic[b])

    ans = c(n, 2)
    # for i in dic:
    #     print(i, dic[i].rank)
    # print()
    for i in dic:
        if dic[i].isParent:
            ans -= c(dic[i].rank, 2)
    print(int(ans))
