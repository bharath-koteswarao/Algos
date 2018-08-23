if __name__ == '__main__':
    n = int(input().strip())
    ans = 0
    level = 1
    while True:
        if (level * (level + 1)) // 2 <= n:
            ans += 1
            n -= (level * (level + 1)) // 2
            level += 1
        else:
            break
    print(ans)
