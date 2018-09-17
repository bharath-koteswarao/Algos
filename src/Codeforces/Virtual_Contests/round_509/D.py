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


if __name__ == '__main__':
    n, h = [int(__) for __ in input().strip().split()]
    arr = []
    for _ in range(n):
        arr.append([int(__) for __ in input().strip().split()])
    arr.sort(key=lambda x: (x[0], x[1]))
    cons = [-arr[0][0]]
    last = 0
    # print(arr)
    for i in range(1, len(arr)):
        cons.append(arr[last][1] - arr[last][0])
        dist = arr[i][0] - arr[last][1]
        if dist > 0:
            cons.append(-1 * dist)
        last += 1
    cons.append(arr[-1][-1] - arr[-1][0])
    # print(cons)
    l, r, ma = get(cons)
    # print(l, r, ma)
    ans = 0
    for i in range(l, r + 1):
        ans += abs(cons[i])
        if cons[i] < 0:
            h += cons[i]
    r += 1
    while h > 0 and r < len(cons):
        if cons[r] > 0:
            ans += cons[r]
        else:
            ans += abs(cons[r])
            h += cons[r]
        r += 1
    if h > 0:
        ans += h
    print(ans)
