def ind(x):
    return x % n


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(i) for i in input().strip().split()]
        inp = [int(i) for i in input().strip().split()]
        p, ne = 0, 0
        for i in inp:
            if i >= 0:
                p += 1
            else:
                ne += 1
        if p == n:
            print(k * sum(inp))
        elif ne == n:
            print(max(inp))
        else:
            l = []
            s = 0
            for i in inp:
                if i >= 0:
                    s += i
                else:
                    l.append(s)
                    l.append(i)
                    s = 0
            if s != 0:
                l.append(s)
            inp = l
            cur, ma = 0, -10000000000
            for i in range(n * k):
                cur += inp[ind(i)]
                ma = max(ma, cur)
                cur = 0 if cur < 0 else cur
            print(ma)
