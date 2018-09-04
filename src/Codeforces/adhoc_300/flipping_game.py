def get(inp):
    cur, ma = 0, -10 ** 10
    l, r, prev = 0, 0, 0
    for i in range(len(inp)):
        if inp[i] == 0:
            cur += 1
        else:
            cur -= 1
        if cur > ma:
            l = prev
            ma = cur
            r = i
        if cur < 0:
            cur = 0
            prev = i + 1
    return l, r, ma


if __name__ == '__main__':
    n = int(input().strip())
    cur, ma = 0, 0
    st, en = 0, 0
    arr = [int(__) for __ in input().strip().split()]
    l, r, maa = get(arr)
    ans = arr.count(1)
    for i in range(l, r + 1):
        if arr[i] == 1:
            ans -= 1
        else:
            ans += 1
    print(ans)
