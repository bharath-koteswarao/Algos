if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in range(1, n + 1)]
    if n == 2:
        print(1)
        print(1, 1)
    elif n == 3:
        print(0)
        print(2, 1, 2)
    else:
        if n % 2 == 0:
            if n % 4 == 0:
                print(0)

