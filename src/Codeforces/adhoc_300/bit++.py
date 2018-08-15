if __name__ == '__main__':
    n = int(input().strip())
    ans = 0
    for _ in range(n):
        st = input().strip()
        ans += 1 if '++' in st else -1
    print(ans)