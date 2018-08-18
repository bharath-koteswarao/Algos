from math import ceil

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    if k > ceil(n / 2):
        print(2 * (k - ceil(n / 2)))
    else:
        print(2 * k - 1)
