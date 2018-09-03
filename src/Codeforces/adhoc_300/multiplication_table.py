if __name__ == '__main__':
    n, x = [int(__) for __ in input().strip().split()]
    ans = 0
    for i in range(1, n + 1):
        if x % i == 0 and i * n >= x:
            ans += 1
    print(ans)