"""
6
1 2 3 4 5 6
4
1 2 5
2 1 4
0 5 4
1 1 6

6
1 2 3 4 5 6
1
1 1 6

"""


class Node:
    even = 0
    odd = 0

    def __repr__(self):
        return "(" + str(self.even) + ", " + str(self.odd) + ")"


def build(segTree, node, start, end):
    if start == end:
        if arr[start] % 2 == 0:
            segTree[node].even = 1
        else:
            segTree[node].odd = 1
    else:
        mid = (start + end) // 2
        build(segTree, (2 * node) + 1, start, mid)
        build(segTree, (2 * node) + 2, mid + 1, end)
        segTree[node].even = segTree[(2 * node) + 1].even + segTree[(2 * node) + 2].even
        segTree[node].odd = segTree[(2 * node) + 1].odd + segTree[(2 * node) + 2].odd


def update(segTree, ind, node, start, end, flag):
    if start == end:
        if flag == 0:
            segTree[node].even += 1
            segTree[node].odd -= 1
        else:
            segTree[node].even -= 1
            segTree[node].odd += 1
    else:
        if flag == 0:
            segTree[node].even += 1
            segTree[node].odd -= 1
        else:
            segTree[node].even -= 1
            segTree[node].odd += 1
        mid = (start + end) // 2
        if ind <= mid:
            update(segTree, ind, (2 * node) + 1, start, mid, flag)
        else:
            update(segTree, ind, (2 * node) + 2, mid + 1, end, flag)


def query(node, l, r, start, end, flag):
    if l == start and r == end:
        if flag == 1:
            return segTree[node].even
        else:
            return segTree[node].odd
    elif l <= start <= end <= r:
        if flag == 1:
            return segTree[node].even
        else:
            return segTree[node].odd
    elif l <= start <= r <= end or start <= l <= end <= r or start <= l <= r <= end:
        mid = (start + end) // 2
        return query((2 * node) + 1, l, r, start, mid, flag) + query((2 * node) + 2, l, r, mid + 1, end, flag)
    else:
        return 0


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    segTree = [Node() for i in range((4 * n))]
    build(segTree, 0, 0, len(arr) - 1)
    q = int(input().strip())
    for _ in range(q):
        f, x, y = [int(i) for i in input().strip().split(" ")]
        if f == 0:
            if not (arr[x - 1] % 2 == y % 2):
                update(segTree, x - 1, 0, 0, n - 1, 0 if y % 2 == 0 else 1)
        elif f == 1:
            ans = query(0, x - 1, y - 1, 0, n - 1, 1)
            print(ans)
        else:
            ans = query(0, x - 1, y - 1, 0, n - 1, 2)
            print(ans)
