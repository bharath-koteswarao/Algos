"""

Input:

3
1
2
3

Output:

2
12
36
"""


def getdiff(n):
    if n <= 10:
        return n if n < 10 else 1
    else:
        lis = [int(i) for i in list(str(n))]
        even, odd = 0, 0
        for i in lis:
            if i % 2 == 0:
                even += i
            else:
                odd += i
        return abs(even - odd)


if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        s, count = 0, 1
        for i in range(2, n + 2):
            s += count * getdiff(i)
            count += 1
        count -= 2
        for i in range(n + 2, 2 * n + 1):
            s += count * getdiff(i)
            count -= 1
        print(s)
