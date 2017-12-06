"""2
10 1
6 5
"""
from math import ceil as c

if __name__ == '__main__':
    tc = int(input().strip())
    s, d = [int(i) for i in input().strip().split(" ")]
    cur = s
    for _ in range(tc - 1):
        s, d = [int(i) for i in input().strip().split(" ")]
        ind = c((cur - s) / d)
        s = s + ind * d
        while s <= cur:
            s += d
        cur = s
    print(cur)
