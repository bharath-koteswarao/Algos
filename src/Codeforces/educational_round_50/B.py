if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, m, k = [int(__) for __ in input().strip().split()]
        if n == m:
            if k == n:
                print(n)
            elif k < n:
                print(-1)
            else:
                dif = k - n
                if dif % 2 == 1:
                    print(n - 1)
                else:
                    print(k)
        else:
            if k == min(n, m) + abs(n - m):
                print(min(n, m))
            elif k < max(n, m):
                print(-1)
            else:
                print(min(n, m) + (k - max(m, n)))
