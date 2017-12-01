def convert(p, q, r, x, y, z, a, b, c, memo):
    if p == x and q == y and r == z:
        return 0
    elif p > x or q > y or r > z:
        return 10 ** 10
    else:
        f = a + convert(p + 1, q, r, x, y, z, a, b, c, memo)
        s = a + convert(p, q + 1, r, x, y, z, a, b, c, memo)
        t = a + convert(p, q, r + 1, x, y, z, a, b, c, memo)
        fo = b + convert(p + 1, q + 1, r, x, y, z, a, b, c, memo)
        fi = b + convert(p, q + 1, r + 1, x, y, z, a, b, c, memo)
        si = b + convert(p + 1, q, r + 1, x, y, z, a, b, c, memo)
        se = c + convert(p + 1, q + 1, r + 1, x, y, z, a, b, c, memo)
        memo[p][q][r] = min(f, s, t, fo, fi, si, se)
        return memo[p][q][r]


if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        x, y, z, a, b, c = [int(i) for i in input().strip().split(" ")]
        memo = [[[-1] * (x + 3)] * (y + 3)] * (z + 3)
        ans = convert(0, 0, 0, x, y, z, a, b, c, memo)
        print(ans)
