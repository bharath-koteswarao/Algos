from math import ceil
if __name__ == '__main__':
    n, m, a = [int(__) for __ in input().strip().split()]
    n = a * ceil(n / a)
    m = a * ceil(m / a)
    print(ceil((n * m) / (a * a)))