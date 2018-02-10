"""
2 4 2
1 0 4 -5
2 1 -7 -2
"""

def getSum(row, start, end):
    su = 0
    for p in range(start, end + 1):
        su += matrix[row][p]
    return su


def kadane(arr):
    cur, ma = 0, -100000000
    for i in arr:
        cur += i
        ma = max(cur, ma)
        cur = 0 if cur < 0 else cur
    return ma


if __name__ == '__main__':
    m, n, k = [int(i) for i in input().strip().split()]
    matrix = []
    for i in range(m):
        matrix.append([int(j) for j in input().strip().split()])
    print(matrix)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            temp = [0 for x in range(m)]
            for x in range(m):
                temp[x] = getSum(x, i, j)
            ans = max(ans, kadane(temp))
    print(ans)
