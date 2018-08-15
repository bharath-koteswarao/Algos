if __name__ == '__main__':
    cur, ans = 0, 0
    for _ in range(int(input().strip())):
        a, b = [int(__) for __ in input().strip().split()]
        cur += b - a
        ans = max(ans, cur)
    print(ans)