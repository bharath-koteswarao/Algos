from bisect import bisect_left as bs
from collections import Counter as cou

if __name__ == '__main__':
    n, d = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    co = cou(arr)
    if d == 0:
        ma = 0
        for i in co:
            ma = max(ma, co[i])
        print(n - ma)
    elif max(arr) - min(arr) <= d:
        print(0)
    else:
        arr.sort()
        mi = 100000
        for i in range(len(arr)):
            idx = bs(arr, arr[i] + d)
            mi = min(mi, n - (idx - i + 1))
        print(mi)
