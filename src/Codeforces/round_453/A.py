if __name__ == '__main__':
    n, des = [int(i) for i in input().strip().split(" ")]
    l = []
    s = set()
    m = 10 ** 10
    ma = 0
    for _ in range(n):
        a, b = [int(i) for i in input().strip().split(" ")]
        m = min(m, a, b)
        ma = max(ma, b)
        l.append([i for i in range(a, b + 1)])
    if m != 0:
        print("NO")
    else:
        if len(l) == 1:
            print("YES" if des in l[0] else "NO")
        else:
            s = set(l[0])
            pos = True
            for i in l:
                if len(s.intersection(i)) > 0:
                    s = s.union(i)
                else:
                    pos = False
                    break
            print("YES" if pos else "NO")
