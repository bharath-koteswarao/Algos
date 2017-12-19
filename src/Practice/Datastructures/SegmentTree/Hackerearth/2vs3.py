"""
10
1011001101
10
0 0 2
"""


class Node:
    st = ""

    def __repr__(self):
        return self.st


def build(start, end, node):
    if start == end:
        segTree[node].st = s[start]
    else:
        mid = (start + end) // 2
        build(start, mid, (2 * node) + 1)
        build(mid + 1, end, (2 * node) + 2)
        segTree[node].st = segTree[(2 * node) + 1].st + segTree[(2 * node) + 2].st


def update(start, end, node, ind):
    if start == end:
        segTree[node].st = '1'
    else:
        mid = (start + end) // 2
        if ind <= mid:
            update(start, mid, 2 * node + 1, ind)
        else:
            update(mid + 1, end, 2 * node + 2, ind)
        segTree[node].st = segTree[2 * node + 1].st + segTree[2 * node + 2].st


def query(l, r, start, end, node):
    if l == start and r == end:
        return segTree[node].st
    elif l <= start <= end <= r:
        return segTree[node].st
    elif l <= start <= r <= end or start <= l <= end <= r or start <= l <= r <= end:
        mid = (start + end) // 2
        return query(l, r, start, mid, 2 * node + 1) + query(l, r, mid + 1, end, 2 * node + 2)
    else:
        return ""


if __name__ == '__main__':
    n = int(input().strip())
    s = list(input().strip())
    segTree = [Node() for i in range(4 * len(s))]
    build(0, n - 1, 0)
    q = int(input().strip())
    for _ in range(q):
        inp = [int(i) for i in input().strip().split(" ")]
        if inp[0] == 1:
            up = inp[1]
            if s[up] == '0':
                s[up] = 1
                update(0, n - 1, 0, up)
        else:
            l, r = inp[1], inp[2]
            bst = query(l, r, 0, n - 1, 0)
            print(int(bst, 2) % 3)
