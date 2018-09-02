if __name__ == '__main__':
    n = int(input().strip())
    nc = n * 1
    ans = 0
    i = 1
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        while n > 0:
            if n >= i:
                n -= i
                ans += 1
            else:
                ans += 1 if nc <= 10 else 0
                break
            i += 1
        print(ans)