from math import floor

"""
5
0 0 0 0 2 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0
1 2 2 3 4 0 3 4 4 1 3 1 4 4 1 0 0 0 0 0 4 2 3 2 2 1
1 1 3 3 1 1 4 4 3 1 3 3 3 0 1 2 0 4 2 1 3 0 3 1 1 1
3 3 0 2 2 2 4 1 2 1 1 1 3 3 0 0 3 2 2 4 1 4 4 1 2 1
2 1 4 1 0 2 0 3 1 2 0 3 1 1 2 0 1 4 2 3 2 3 2 0 2 1
"""

"""
1
25
24
25
21
"""

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        l = [int(__) for __ in input().strip().split()]
        su = sum(l)
        print(floor(su / 2) if su % 2 == 1 else su // 2 - 1)
