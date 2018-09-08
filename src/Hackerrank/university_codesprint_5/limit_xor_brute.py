if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    ans = 0
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            xr = arr[j]
            for p in range(j + 1, j + i):
                xr ^= arr[p]
            if xr < k:
                ans += 1
            # print(arr[j: j + i], xr < k, xr, k)
    print(ans)
