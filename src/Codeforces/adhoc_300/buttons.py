if __name__ == '__main__':
    n = int(input().strip())
    if n == 1:
        print(1)
    else:
        ans = n * 1
        st = 2
        n -= 2
        while n > 0:
            ans += n * st + 1
            n -= 1
            st += 1
        print(ans + 1)
