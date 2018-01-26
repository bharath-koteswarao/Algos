from math import gcd as getGcd


class Node:
    gcd = 0
    count = 0

    def __repr__(self):
        return str(self.gcd)


def build(start, end, node):
    if start == end:
        segTree[node].gcd = arr[start]
        if arr[start] == 1:
            segTree[node].count = 1
        else:
            segTree[node].count = 0
    else:
        mid = (start + end) // 2
        build(start, mid, (2 * node) + 1)
        build(mid + 1, end, (2 * node) + 2)
        segTree[node].gcd = getGcd(segTree[(2 * node) + 1].gcd, segTree[(2 * node) + 2].gcd)
        # segTree[node].count = segTree[2 * node + 1].count + segTree[2 * node + 2].count


def query(l, r, start, end, g, node):
    if l == start and r == end:
        if segTree[node].gcd == g:
            return 0
        else:
            return 1
    elif l <= start <= end <= r:
        if segTree[node].gcd == g:
            return 0
        else:
            return 1
    elif l <= start <= r <= end or start <= l <= end <= r or start <= l <= r <= end:
        mid = (start + end) // 2
        return query(l, r, start, mid, g, 2 * node + 1) + query(l, r, mid + 1, end, g, 2 * node + 2)
    else:
        return 0


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    segTree = [Node() for i in range(4 * n)]
    build(0, n - 1, 0)
    print(segTree)
    tc = int(input().strip())
    for _ in range(tc):
        inp = [int(i) for i in input().strip().split()]
        if inp[0] == 1:
            f, l, r, g = inp
            res = query(l - 1, r - 1, 0, n - 1, g, 0)
            print(res)
