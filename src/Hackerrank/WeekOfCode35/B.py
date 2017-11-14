if __name__ == '__main__':
    n, m, k = [int(i) for i in input().strip().split(" ")]
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if i == 0 and j == 0:
                mat[i][j] = m
            elif i == j and i != 0:
                mat[i][j] = mat[i - 1][j - 1] + k
            elif i > j:
                mat[i][j] = mat[i - 1][j] - 1
            elif i < j:
                mat[i][j] = mat[i][j - 1] - 1
    for i in range(0, n):
        for j in range(0, n):
            print(mat[i][j], end=" ")
        print()
