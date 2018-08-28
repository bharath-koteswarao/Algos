if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    mat = []
    for _ in range(n):
        mat.append(list(input().strip()))
    x, y = 0, 0
    found = False
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'B':
                x, y = i, j
                found = True
                break
        if found:
            break
    xc, yc = 0, 0
    for i in range(x, n):
        if mat[i][y] == 'B':
            xc += 1
        else:
            break
    for j in range(y, m):
        if mat[x][j] == 'B':
            yc += 1
        else:
            break
    print(x + (xc // 2) + 1, y + (yc // 2) + 1)
