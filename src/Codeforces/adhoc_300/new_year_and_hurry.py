if __name__ == '__main__':
    n, p = [int(__) for __ in input().strip().split()]
    p = 4 * 60 - p
    k = 1
    while k * (k + 1) <= p * 0.4:
        k += 1
    print(min(k if k * (k + 1) <= p * 0.4 else k - 1, n))
