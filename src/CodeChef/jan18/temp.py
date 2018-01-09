if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(i) for i in input().strip().split()]
        inp = [int(i) for i in input().strip().split()]
        p, ne = 0, 0
        inp = inp * k
        cur, ma = 0, -10 ** 10
        for i in inp:
            if i >= 0:
                p += 1
            else:
                ne += 1
            cur += i
            ma = max(ma, cur)
            if cur < 0:
                cur = 0
        print(ma if ne < n * k else max(inp))
