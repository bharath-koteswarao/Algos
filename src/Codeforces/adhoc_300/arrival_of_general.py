if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ma, mi = max(arr), min(arr)
    idx1, idx2 = 0, 0
    for i in range(n):
        if arr[i] == ma:
            idx1 = i
            break
    for i in range(n - 1, -1, -1):
        if arr[i] == mi:
            idx2 = i
            break
    ans = 0
    if idx1 > idx2:
        ans -= 1
    ans += idx1
    ans += n - (idx2 + 1)
    print(ans)
