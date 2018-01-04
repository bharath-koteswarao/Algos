"""16 8 7 4 3 2 1"""
from bisect import bisect_left as bs


class Node:
    lis = []

    def __init__(self, lis):
        self.lis = lis

    def __repr__(self):
        return str(self.lis)


def merge(l1, r1, l2, r2):
    i, j, k = l1, l2, l1
    temp = []
    while i <= r1 and j <= r2:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= r1:
        temp.append(arr[i])
        i += 1
    while j <= r2:
        temp.append(arr[j])
        j += 1
    for i in range(len(temp)):
        arr[k] = temp[i]
        k += 1
    return temp


def mergeSort(arr, l, r, node):
    if l != r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid, 2 * node + 1)
        mergeSort(arr, mid + 1, r, 2 * node + 2)
        t = merge(l, mid, mid + 1, r)
        segTree[node] = Node(t)
    else:
        segTree[node] = Node([arr[l]])


def query(l, r, start, end, k, node):
    cur = segTree[node].lis
    if l == start and r == end:
        return len(cur) - bs(cur, k + 0.1)
    elif l <= start <= end <= r:
        return len(cur) - bs(cur, k + 0.1)
    elif l <= start <= r <= end or start <= l <= end <= r or start <= l <= r <= end:
        mid = (start + end) // 2
        return query(l, r, start, mid, k, 2 * node + 1) + query(l, r, mid + 1, end, k, 2 * node + 1)
    else:
        return 0


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    segTree = [Node([]) for i in range(4 * len(arr))]
    mergeSort(arr, 0, len(arr) - 1, 0)
    for i in range(int(input().strip())):
        l, r, k = [int(i) for i in input().strip().split()]
        l, r = l - 1, r - 1
        print(query(l, r, 0, n - 1, k, 0))
