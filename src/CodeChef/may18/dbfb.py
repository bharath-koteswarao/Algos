if __name__ == '__main__':
    mod = 10 ** 9 + 7
    for _ in range(int(input().strip())):
        m, n = [int(__) for __ in input().strip().split()]
        arr1 = [int(__) for __ in input().strip().split()]
        arr2 = [int(__) for __ in input().strip().split()]
        s1, s2 = sum(arr1), sum(arr2)
        fib = [(1, 0), (0, 1)]
        for k in range(2, n):
            fib.append((fib[k - 1][0] + fib[k - 2][0], fib[k - 1][1] + fib[k - 2][1]))
        l1, l2 = fib[-1]
        print(m * (l1 * s1 + l2 * s2) % mod)
