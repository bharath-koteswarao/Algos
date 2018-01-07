if __name__ == '__main__':
    for _ in range(int(input().strip())):
        x, n = [int(i) for i in input().strip().split()]
        if n <= 3:
            print("impossible")
        elif (n % 4 == 0 or n % 4 == 3) and (x % 2 != 0):
            print("impossible")
        elif (n % 4 == 1 or n % 4 == 2) and x % 2 != 1:
            print("impossible")
        else:
            s = n * (n + 1) // 2 - x
            s //= 2
