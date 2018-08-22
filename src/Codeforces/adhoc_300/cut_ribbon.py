import sys
def getAns(n, arr, memo):
    if n in memo:
        return memo[n]
    else:
        if n == 0:
            return 1
        elif n < 0:
            return -float('inf')
        else:
            a = getAns(n - arr[0], arr, memo)
            b = getAns(n - arr[1], arr, memo)
            c = getAns(n - arr[2], arr, memo)
            memo[n] = 1 + max(a, b, c)
            return 1 + max(a, b, c)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    n, a, b, c = [int(__) for __ in input().strip().split()]
    arr = [a, b, c]
    memo = {}
    ans = getAns(n, arr, memo)
    print(ans - 1)
