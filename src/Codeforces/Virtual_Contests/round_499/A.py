def wt(s):
    return ord(s) - ord('a') + 1


if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    inp = sorted(list(input().strip()))
    ans = wt(inp[0])
    last = ans
    k -= 1
    for i in range(1, n):
        if wt(inp[i]) - last > 1:
            k -= 1
            ans += wt(inp[i])
            last = wt(inp[i])

        if k <= 0:
            break
    print(ans if k <= 0 else -1)
