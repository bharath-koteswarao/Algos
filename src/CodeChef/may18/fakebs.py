"""
1
7 7
3 1 6 7 2 5 4
1
2
3
4
5
6
7

1
7 1
10 3 5 2 1 0 8
1
"""


class Node:
    cl, cr = 0, 0
    ans = 0

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    def __repr__(self):
        return '(' + str(self.val) + ',' + str(self.idx) + ',' + str(self.cl) + ',' + str(self.cr) + ')'


def build(start, end, arr, idx, dic, tree):
    if idx < len(tree):
        if start == end:
            dic[arr[start]] = Node(arr[start], idx)
            tree[idx] = arr[start]
        elif start <= end:
            mid = (start + end) // 2
            dic[arr[mid]] = Node(arr[mid], idx)
            tree[idx] = arr[mid]
            build(start, mid - 1, arr, 2 * idx + 1, dic, tree)
            build(mid + 1, end, arr, 2 * idx + 2, dic, tree)


def construct(start, end, node, arr, dic, tree):
    if start <= end:
        mid = (start + end) // 2
        dic[arr[mid]] = Node(arr[mid], node)
        tree[node] = arr[mid]
        # print(mid + 1, node)
        construct(start, mid - 1, 2 * node + 1, arr, dic, tree)
        construct(mid + 1, end, 2 * node + 2, arr, dic, tree)


def get_path(idx):
    l = []
    while idx != 0:
        l.append(idx)
        idx = (idx - 1) // 2
    l.append(0)
    return l[::-1]


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, q = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        queries = []
        for __ in range(q):
            queries.append(int(input().strip()))
        tree = [0 for i in range(4 * n)]
        dic = {}
        sor_dic = {}
        so = sorted(arr)
        for x in range(len(so)):
            sor_dic[so[x]] = x
        # build(0, n - 1, arr, 0, dic, tree)
        construct(0, n - 1, 0, arr, dic, tree)
        for val in dic:
            cl, cr = 0, 0
            path = get_path(dic[val].idx)
            for i in range(len(path) - 1):
                left = path[i + 1] == (2 * path[i] + 1)
                nod = tree[path[i]]
                if val > nod:
                    cr += 1 if left else 0
                else:
                    cl += 1 if not left else 0
            dic[val].cl = cl
            dic[val].cr = cr
        # print(dic)
        for val in dic:
            cl, cr = dic[val].cl, dic[val].cr
            if sor_dic[val] >= cl and n - sor_dic[val] - 1 >= cr:
                dic[val].ans = max(cl, cr)
            else:
                dic[val].ans = -1
        for query in queries:
            print(dic[query].ans)
