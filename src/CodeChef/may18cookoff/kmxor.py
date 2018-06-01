def rev(num):
    ret = []
    for i in range(len(num)):
        if num[i] == '1':
            ret.append('0')
        else:
            ret.append('1')
    return ret


def prt(mat):
    for p in mat:
        for q in p:
            print(q, end=" ")
        print()


def even(mat, lim):
    mat[0] = rev(num)
    for i in range(lim):
        if num[i] == '0':
            for j in range(1, len(mat)):
                mat[j][i] = '0'
    if int(''.join(mat[0]), 2) == 0:
        mat[0][0] = '1'
        mat[1][0] = '0'
    return mat


def get_count(mat):
    ret = [0 for i in range(len(mat[0]))]
    for i in range(len(mat[0])):
        count = 0
        for j in range(len(mat)):
            if mat[j][i] == '1':
                count += 1
        ret[i] = count
    return ret


def show(mat):
    for i in mat:
        print(int(''.join(i), 2), end=" ")
    print()


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(__) for __ in input().strip().split()]
        le = len(bin(k)[2:])
        mat = [['1' for i in range(le)] for j in range(n)]
        num = list(bin(k)[2:])
        if k == 1:
            for i in range(n):
                print(1, end=" ")
            print()
        else:
            if n == 1:
                print(k)
            else:
                if n % 2 == 0:
                    mat = even(mat, le)
                    show(mat)
                else:
                    for i in range(le - 1, -1, -1):
                        if num[i] == '0':
                            mat[0][i] = '1'
                            mat[0][0] = '0'
                    for i in range(le - 1, -1, -1):
                        for j in range(1, n):
                            if num[i] == '0':
                                mat[j][i] = '0'
                    ct = get_count(mat)
                    if ct[0] % 2 == 0:
                        for i in range(n):
                            if mat[i][0] == '1':
                                mat[i][0] = '0'
                                break
                    show(mat)
