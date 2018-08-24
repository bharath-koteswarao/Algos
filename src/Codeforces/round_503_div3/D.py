if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    ma = 0
    for x in arr:
        ma = max(ma, len(str(x)))
    di = {}
    for x in arr:
        if len(str(x)) not in di:
            re = x % k
            di[len(str(x))] = [x % k]
        else:
            re = x % k
            di[len(str(x))].append(x % k)
    ans = 0
    for x in arr:
        for i in range(1, ma + 1):
            re = x * (10 ** i) % k