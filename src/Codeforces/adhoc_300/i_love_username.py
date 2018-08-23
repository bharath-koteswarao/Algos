if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ma = mi = arr[0]
    ans = 0
    for i in range(1, n):
        if arr[i] > ma:
            ans += 1
            ma = arr[i]
        elif arr[i] < mi:
            ans += 1
            mi = arr[i]
    print(ans)
