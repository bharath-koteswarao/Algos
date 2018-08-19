if __name__ == '__main__':
    n = int(input().strip())
    ans = 1
    l = []
    for _ in range(n):
        l.append(input().strip())
    prev = l[0]
    for i in range(1, n):
        if l[i] != prev:
            ans += 1
            prev = l[i]
    print(ans)
