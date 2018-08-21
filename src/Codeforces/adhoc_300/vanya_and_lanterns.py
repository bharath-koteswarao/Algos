if __name__ == '__main__':
    l, n = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    arr.sort()
    ans = 0
    for i in range(l - 1):
        ans = max(ans, arr[i + 1] - arr[i])
    print(max(ans / 2, arr[0], n - arr[-1]))
