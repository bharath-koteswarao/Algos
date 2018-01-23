class Node:
    pf = {}
    lis = []

    def __init__(self, pf):
        self.pf = pf

    def __repr__(self):
        return str(self.pf) + str(self.lis)


def getPf(n):
    if n == 1:
        return {1: 1}
    else:
        dic = {}
        c = 0
        while n % 2 == 0 and n != 0:
            c += 1
            n //= 2
        if c > 0:
            dic[2] = c
        for i in range(3, int(n ** 0.5) + 1):
            c = 0
            while n % i == 0 and n != 0:
                c += 1
                n //= i
            if c > 0:
                dic[i] = c
        if n > 1:
            dic[n] = 1
        return dic


def build(segTree, start, end, node):
    if start == end:
        segTree[node] = Node(getPf(arr[start]))
    else:
        mid = (start + end) // 2
        build(segTree, start, mid, 2 * node + 1)
        build(segTree, mid + 1, end, 2 * node + 2)
        # segTree[node].lis.append(segTree[2 * node + 1].pf)
        # segTree[node].lis.append(segTree[2 * node + 2].pf)


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    segTree = [0] * 4 * n
    build(segTree, 0, n - 1, 0)
    print(segTree)
