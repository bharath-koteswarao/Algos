if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    cur = 1
    ans = 0
    for i in range(m):
        if arr[i] != cur:
            if arr[i] > cur:
                ans += arr[i] - cur
            else:
                ans += arr[i] + n - cur
            cur = arr[i]
    print(ans)