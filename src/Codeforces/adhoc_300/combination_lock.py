if __name__ == '__main__':
    n = int(input().strip())
    n1 = [int(__) for __ in list(input().strip())]
    n2 = [int(__) for __ in list(input().strip())]
    ans = 0
    for i in range(n):
        a, b = n1[i], n2[i]
        ans += min(abs(a - b), 9 - a + b + 1, 9 - b + a + 1)
    print(ans)
