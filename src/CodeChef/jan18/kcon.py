def get(inp):
    cur, ma = 0, -10 ** 10
    l, r, prev = 0, 0, 0
    for i in range(len(inp)):
        cur += inp[i]
        if cur > ma:
            l = prev
            ma = cur
            r = i
        if cur < 0:
            cur = 0
            prev = i + 1
    return l, r, ma


if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n, k = [int(i) for i in input().strip().split()]
        arr = [int(i) for i in input().strip().split()]
        pe, ne = 0, 0
        for i in arr:
            if i >= 0:
                pe += 1
            else:
                ne += 1
        if ne == n:
            print(max(arr))
        elif pe == n:
            print(sum(arr) * k)
        else:
            l1, r1, ma1 = get(arr)
            if k == 1:
                print(ma1)
            else:
                l2, r2, ma2 = get(arr + arr)
                if l2 == 0 and r2 == 2 * n - 1:
                    print(k * ma1)
                elif l2 == 0 and r2 < 2 * n - 1:
                    bar = sum(arr[r1 + 1:])
                    print(k * ma1 + (k - 1) * bar)
                elif l2 != 0 and r2 != 2 * n - 1:
                    print(ma2)
                else:
                    bar = sum(arr[:l1])
                    print(k * ma1 + (k - 1) * bar)
