if __name__ == '__main__':
    mod = 10 ** 9 + 7
    for _ in range(int(input().strip())):
        m, n = [int(__) for __ in input().strip().split()]
        a = [int(__) for __ in input().strip().split()]
        b = [int(__) for __ in input().strip().split()]
        res = 0
        for i in range(m):
            for j in range(m):
                fib = [a[i], b[j]]
                for k in range(2, max(2, n)):
                    fib.append(fib[k - 1] + fib[k - 2])
                res += fib[n - 1] % mod
                print(fib)
        print(res % mod)