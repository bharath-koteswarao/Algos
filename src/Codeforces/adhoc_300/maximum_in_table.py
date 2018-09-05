if __name__ == '__main__':
    n = int(input().strip())
    table = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        table[i][0] = 1
        table[0][i] = 1
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
            ans = max(ans, table[i][j])
    print(ans if n > 1 else 1)
