if __name__ == '__main__':
    n = int(input().strip())
    arr = [5, 4, 3, 2, 1]
    ans = 0
    for i in arr:
        if n == 0:
            break
        ans += n // i
        n %= i
    print(ans)