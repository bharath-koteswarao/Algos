def getAdj(node):
    a, b = node
    ps = [(a - 2, b - 1), (a - 2, b + 1), (a, b + 2), (a + 2, b + 1), (a + 2, b - 1), (a, b - 2)]
    adj = []
    for i in ps:
        p, q = i
        if p < n and q < n and p >= 0 and q >= 0:
            if not vm[p][q]:
                adj.append(i)
    return adj


def getDir(this, prev):
    a, b = this
    c, d = prev
    if a < c and b < d:
        return "UL"
    elif a < c and b > d:
        return "UR"
    elif a == c and b < d:
        return "L"
    elif a == c and b > d:
        return "R"
    elif a > c and b < d:
        return "LL"
    elif a > c and b > d:
        return "LR"


if __name__ == '__main__':
    n = int(input().strip())
    x1, y1, x2, y2 = [int(i) for i in input().strip().split(" ")]
    mat = [[0 for j in range(n)] for i in range(n)]
    vm = [[False for j in range(n)] for i in range(n)]
    found = False
    cur = [(x1, y1)]
    levels = 0
    dic, dist = {}, -1
    paths = {(x1, y1): (x1, y1)}
    while len(cur) != 0:
        nex = []
        for p in cur:
            vm[p[0]][p[1]] = True
            adj = getAdj(p)
            for nei in adj:
                if nei not in nex:
                    if nei not in paths:
                        paths[nei] = p
                    if nei == (x2, y2):
                        found = True
                        dist = levels
                    nex.append(nei)
        cur = nex
        levels += 1
        if len(cur) != 0:
            dic[levels] = cur
    if not found:
        print("Impossible")
    else:
        print(dist)
        path = []
        s = (x2, y2)
        path.append(s)
        while True:
            s = paths[s]
            if s == (x1, y1):
                break
            else:
                path.append(s)
        prev = (x1, y1)
        for i in range(len(path) - 1, -1, -1):
            di = getDir(path[i], prev)
            prev = path[i]
            print(di, end=' ')
