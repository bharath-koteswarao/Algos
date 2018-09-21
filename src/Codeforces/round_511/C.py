def gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd


def get(inp):
    cur, ma = 0, -10 ** 10
    l, r, prev = 0, 0, 0
    for i in range(len(inp)):
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
    g = 0
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ma, cur = 0, 0
    for x in arr:
        g = gcd(g, x)
        if g > 1:
            cur += 1
            ma = max(cur, ma)
        else:
            cur = 0
            g = 0
    if ma == 0:
        print(-1)
    else:
        print(n - ma)
