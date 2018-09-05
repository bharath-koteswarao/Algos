def get(n, m, k):
    return 2 * m * k - n, n - m * k


if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    for k in range(int(n / (2 * m)), 100001, 1):
        a, b = get(n, m, k)
        if a >= 0 and b >= 0 and (a + b) > 0 and (a + b) % m == 0:
            print(a + b)
            exit(0)
        if b < 0:
            break
    print(-1)
