if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        arr.sort()
        ans = arr[-1] - arr[0]
        for i in range(n - 1):
            ans = min(ans, arr[i + 1] - arr[i])
        print(ans)