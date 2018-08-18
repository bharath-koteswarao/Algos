from math import ceil

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    if k <= n:
        print(ceil(k / 2) - 1)
    elif k >= 2 * n:
        print(0)
    else:
        le = n - (k // 2)
        print(le)
