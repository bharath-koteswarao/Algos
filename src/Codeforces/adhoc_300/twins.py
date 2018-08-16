if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    arr.sort(reverse=True)
    half = sum(arr) / 2
    ans = 0
    su = 0
    for x in arr:
        ans += 1
        if su + x > half:
            break
        su += x
    print(ans)