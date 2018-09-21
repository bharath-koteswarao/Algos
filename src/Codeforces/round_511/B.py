from math import *

if __name__ == '__main__':
    n = int(input().strip())
    dist = 0
    x, y = 0, 0
    for _ in range(n):
        a, b = [int(__) for __ in input().strip().split()]
        cur = sqrt(pow(a, 2) + pow(b, 2))
        if cur > dist:
            dist = cur
            x, y = a, b
    print(x + y)
