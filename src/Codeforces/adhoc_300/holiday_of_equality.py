if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ma = max(arr)
    ans = 0
    for x in arr:
        ans += abs(x - ma)
    print(ans)