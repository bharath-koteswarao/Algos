if __name__ == '__main__':
    n = int(input().strip())
    s1 = input().strip()
    s2 = input().strip()
    dif = []
    for i in range(n):
        if s1[i] != s2[i]:
            dif.append(i + 1)
    ans = 0
    if s1.count('1') == s2.count('1'):
        ans = 0
        for i in range(0, len(dif) - 1, 2):
            ans += min(dif[i + 1] - dif[i], 2)
        print(ans)
    else:
        print(dif)
        ans = abs(s1.count('1') - s2.count('1'))
        for i in range(ans, len(dif) - 1):
            ans += min(dif[i + 1] - dif[i], 2)
        print(ans)
