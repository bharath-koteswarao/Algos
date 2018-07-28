from math import ceil, floor

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        l, r = [int(__) for __ in input().strip().split()]
        l = ceil(l ** 0.5)
        r = floor(r ** 0.5)
        print(r - l + 1)