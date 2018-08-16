if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    arr.sort()
    ans = arr[-1] - arr[0]
    for i in range(len(arr) - n + 1):
        ans = min(ans, arr[i + n - 1] - arr[i])
    print(ans)