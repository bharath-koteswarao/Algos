if __name__ == '__main__':
    n, k = [int(i) for i in input().strip().split()]
    bi = list(bin(n)[2:])
    l = len(bi)
    if k == 1:
        print(n)
    else:
        print(2 ** l - 1)
