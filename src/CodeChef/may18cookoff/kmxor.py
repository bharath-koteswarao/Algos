if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    le = len(bin(k)[2:])
    mat = [['0' for i in range(le)] for j in range(n)]
    inc = True
    x = 0
    for y in range(le):
        mat[x][y] = '1'
        if x == n - 1:
            inc = not inc
        if inc:
            x += 1
        else:
            x -= 1
    for x in mat:
        print(int(''.join(x), 2), end=' ')
