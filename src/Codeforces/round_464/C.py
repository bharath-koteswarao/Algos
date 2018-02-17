if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    f, s = [int(i) for i in input().strip().split()]
    win = s - f
    arr = arr + arr
    if win >= len(arr):
        print(1)
    else:
        pre = [arr[0]]
        for i in range(1, len(arr)):
            pre.append(arr[i] + pre[i - 1])
        ma = pre[win - 1]
        ind = 0
        for i in range(1, n):
            if pre[i + win - 1] - pre[i - 1] > ma:
                ind = i
                ma = pre[i + win - 1] - pre[i - 1]
        ans = f
        ans += n - ind
        if ans <= n:
            print(ans)
        else:
            print(ans % n)
