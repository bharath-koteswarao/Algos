if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ma, cur = 0, 0
    for i in range(n - 1):
        if arr[i + 1] >= arr[i]:
            cur += 1
            ma = max(ma, cur)
        else:
            cur = 0
    print(ma + 1)