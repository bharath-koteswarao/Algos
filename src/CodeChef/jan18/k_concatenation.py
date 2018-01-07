"""
1
10 35
100 -1 -2 -3 4 5 6 -70 -80 90

"""
def get(inp):
    cur, ma = 0, -10 ** 10
    l, r, prev = 0, 0, 0
    for i in range(n):
        cur += inp[i]
        if cur > ma:
            l = prev
            ma = cur
            r = i
        if cur < 0:
            cur = 0
            prev = i + 1
    return l, r, ma


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
            l, r, ma1 = get(inp)
            if k == 1:
                print(ma1)
            else:
                bar = 0
                if l == 0 and r != n - 1:
                    inp = inp[r + 1:] + inp[l:r + 1]
                    print(inp)
                    l, r, ma = get(inp)
                    print(l,r,ma)
                    bar = sum(inp[:l])
                    if abs(bar) >= ma:
                        print(ma)
                    else:
                        print(ma * k + (k - 1) * bar - (ma - ma1))
                    pass
                elif l != 0 and r == n - 1:
                    inp = inp[l:] + inp[:l]
                    l, r, ma = get(inp)
                    bar = sum(inp[r + 1:])
                    if abs(bar) >= ma:
                        print(ma)
                    else:
                        print(k * ma + (k - 1) * bar - (ma - ma1))
                    pass
                elif l == 0 and r == n - 1:
                    print(ma1 * k)
                else:
                    inp = inp[l:] + inp[:l]
                    l, r, ma = get(inp)
                    print(inp)
                    bar = sum(inp[r + 1:])
                    p, q = 0, 0
                    if abs(bar) >= ma:
                        p = ma
                    else:
                        p = k * ma + (k - 1) * bar - (ma - ma1)
                    inp2 = inp[r + 1:] + inp[:r + 1]
                    l, r, ma2 = get(inp2)
                    bar2 = sum(inp2[:l])
                    if abs(bar2) >= ma2:
                        q = ma2
                    else:
                        q = k * ma2 + (k - 1) * bar2 - (ma2 - ma1)
                    print(inp2)
                    print(max(p, q))
                    pass
