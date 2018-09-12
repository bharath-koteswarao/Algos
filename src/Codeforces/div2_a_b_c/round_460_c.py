if __name__ == '__main__':
    n, m, k = [int(__) for __ in input().strip().split()]
    arr = []
    ans = 0
    for _ in range(n):
        arr.append(list(input().strip()))
    if k == 1:
        ans = 0
        for x in arr:
            ans += x.count('.')
        print(ans)
        exit(0)
    if n == 1 and m == 1 and k == 1:
        if arr[0][0] == '.':
            print(1)
        else:
            print(0)
    else:
        for i in range(n):
            j = 0
            count = 0
            while j < m:
                if arr[i][j] == '.':
                    count += 1
                else:
                    if count >= k:
                        ans += count - k + 1
                    count = 0
                j += 1
            if count >= k:
                ans += count - k + 1
        for i in range(m):
            j = 0
            count = 0
            while j < n:
                if arr[j][i] == '.':
                    count += 1
                else:
                    if count >= k:
                        ans += count - k + 1
                    count = 0
                j += 1
            if count >= k:
                ans += count - k + 1
        print(ans)
