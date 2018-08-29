if __name__ == '__main__':
    n, p, q, r = [int(__) for __ in input().strip().split()]
    su = 0
    a1 = [int(__) for __ in input().strip().split()]
    a2 = [p, q, r]
    for x in a2:
        ma = -10 ** 20
        for y in a1:
            ma = max(ma, x * y)
        su += ma
    print(su)
