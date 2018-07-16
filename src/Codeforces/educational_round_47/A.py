if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    c = [int(__) for __ in input().strip().split()]
    a = [int(__) for __ in input().strip().split()]
    ans = 0
    ci, ai = 0, 0
    while ci < n and ai < m:
        if a[ai] >= c[ci]:
            ai += 1
            ci += 1
            ans += 1
        else:
            ci += 1
    print(ans)
