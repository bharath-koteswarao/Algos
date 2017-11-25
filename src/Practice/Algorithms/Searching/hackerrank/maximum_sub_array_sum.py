if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n, m = [int(i) for i in input().strip().split(" ")]
        inp = [int(i) for i in input().strip().split(" ")]
        ma, c, t = 0, 0, 0
        for i in range(len(inp)):
            c += inp[i]
            t += inp[i]
            if c >= m:
                c = 0
            ma = max(c, ma, t % m)
        print(ma)
