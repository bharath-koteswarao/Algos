if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        total = (n * (n + 1)) // 2
        s = 1
        ans = 0
        for i in range(1, n):
            ans += i * (total - s)
            s += (i + 1)
        print(ans)
