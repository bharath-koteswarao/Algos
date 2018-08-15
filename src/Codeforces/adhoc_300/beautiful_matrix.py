if __name__ == '__main__':
    mat = []
    mid = (2, 2)
    for _ in range(5):
        mat.append([int(__) for __ in input().strip().split()])
    given = 0
    for i in range(5):
        for j in range(5):
            if mat[i][j] == 1:
                given = (i, j)
                break
    print(abs(mid[0] - given[0]) + abs(mid[1] - given[1]))