if __name__ == '__main__':
    n, m, x = [int(__) for __ in input().strip().split()]
    s = [int(__) for __ in input().strip().split()]
    t = [int(__) for __ in input().strip().split()]
    s.sort()
    t.sort()
    for i in range(1, n):
        while s[i] - x >= s[i - 1] and t[i] - x >= t[i - 1]:
            s[i] -= x
            t[i] -= x
    print(
        max(s) + max(t) - (min(s) + min(t))
    )
