def getInd(n):
    return n % m


def dist(t1, t2):
    a,b = t1
    c,d = t2



if __name__ == '__main__':
    n, m, k = [int(i) for i in input().strip().split()]
    l = []
    for _ in range(m):
        a, b = [int(i) for i in input().strip().split()]
        l.append((a, b, a + b if a >= b else -(a + b)))
    l.sort(key=lambda x: x[2])
    mi = 10 ** 10
    for i in range(m):
        # print(abs(l[i][2] - l[getInd(i + 2)][2]))
        mi = min(mi, dist(l[i],l[getInd(i+k-1)]))
    print(mi)
