if __name__ == '__main__':
    n = int(input().strip())
    s1 = [int(__) for __ in list(input().strip())]
    s2 = [int(__) for __ in list(input().strip())]
    ans = 0
    for i in range(n):
        if s1[i] != s2[i]:
            if i + 1 < n and s1[i + 1] != s2[i + 1] and s1[i] != s1[i + 1]:
                ans += 1
                s1[i] = 1 - s1[i]
                s1[i + 1] = 1 - s1[i + 1]
            else:
                ans += 1
                s1[i] = 1 - s1[i]
    print(ans)
