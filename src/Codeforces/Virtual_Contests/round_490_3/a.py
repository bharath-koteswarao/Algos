if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    ans = 0
    while True and len(arr) > 0:
        if arr[0] <= k:
            ans += 1
            arr = arr[1:]
        else:
            break
    arr = arr[::-1]
    while True and len(arr) > 0:
        if arr[0] <= k:
            ans += 1
            arr = arr[1:]
        else:
            break
    print(ans)
