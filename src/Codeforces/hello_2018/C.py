from math import ceil
from math import log

if __name__ == '__main__':
    n, l = [int(i) for i in input().strip().split()]
    c = [int(i) for i in input().strip().split()]
    l2 = 0
    if log(l, 2) != int(log(l, 2)):
        l2 = 2 ** ceil(log(l, 2))
    cost = {}
    for i in range(n):
        c[i] = (2 ** i, c[i])
        cost[2 ** i] = c[i][1]
    c.sort(key=lambda x: (x[1], x[0]))

