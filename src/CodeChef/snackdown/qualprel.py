from bisect import bisect_left as bs

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        el = sorted(arr, reverse=True)[k - 1]
        arr.sort()
        idx = bs(arr, el)
        print(n - idx)
