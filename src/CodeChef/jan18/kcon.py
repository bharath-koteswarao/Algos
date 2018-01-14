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
                if l1 == 0 and r1 < n - 1:
                    l11, r11, ma11 = get(arr[r1 + 1:] + arr[:l1 + 1])
                    print(arr[r1 + 1:] + arr[:l1 + 1])
                    if ma11 >= ma1:
                        bar = sum(arr[r1 + 1:r1 + 1 + l11])
                        if abs(bar) < ma1:
                            print(k * ma1 + (k - 1) * sum(arr[r1 + 1:]))
                        elif ma1 <= abs(bar) < ma11:
                            print((k - 1) * ma11 + (k - 2) * bar)
                        else:
                            print(ma11)
                    else:
                        print(ma1)
                elif l1 > 0 and r1 < n - 1:
                    pass
                    pass
                elif l1 > 0 and r1 == n - 1:
                    pass
                    pass
