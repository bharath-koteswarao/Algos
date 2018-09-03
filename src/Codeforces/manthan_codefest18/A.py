if __name__ == '__main__':
    n = int(input().strip())
    ans = 0
    i = 1
    while n > 0:
        ans += 1
        n -= i
        i *= 2
    print(ans)
