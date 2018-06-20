if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k, m = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        su = 0
        ans = 0
        for i in range(len(arr)):
            if su + arr[i] >= k:
                ans = i + 1
                break
            else:
                su += arr[i]
        print(ans)