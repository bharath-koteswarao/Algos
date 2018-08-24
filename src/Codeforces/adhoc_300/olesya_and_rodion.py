if __name__ == '__main__':
    n, t = [int(__) for __ in input().strip().split()]
    if t == 10:
        if n == 2:
            print(10)
        elif n < 2:
            print(-1)
        else:
            print('1' + (n - 1) * '0')
    else:
        print(str(t) * n)
