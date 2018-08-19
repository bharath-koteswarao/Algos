if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for _ in range(n):
        a, b = [int(__) for __ in input().strip().split()]
        dic[_ + 1] = (a, b)
    ans = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if dic[i][0] == dic[j][1]:
                ans += 1
            if dic[i][1] == dic[j][0]:
                ans += 1
    print(ans)
