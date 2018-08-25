import sys


def getAns(su, arr, count, memo):
    if su in memo:
        return memo[su]
    else:
        if su in arr:
            memo[su] = count + 1
            return memo[su]
        elif su == 0:
            return 0
        else:
            mi = float('inf')
            for x in arr:
                if su - x > 1:
                    mi = min(mi, getAns(su - x, arr, count + 1, memo))
            memo[su] = mi
            return memo[su]


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    arr = [2, 3, 5, 7]
    tc = int(input().strip())
    for _ in range(tc):
        memo = {}
        su = int(input().strip())
        ans = getAns(su, arr, 0, memo)
        print(ans)
