def get(k, n):
    su, i = 0, 1
    while i <= n:
        su += i
        i *= k
        i += 1
    return su


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        k, a, b = [int(i) for i in input().strip().split()]
        ans = 0
        for i in range(a, b + 1):
            ans += get(k, i)
        print(ans)
