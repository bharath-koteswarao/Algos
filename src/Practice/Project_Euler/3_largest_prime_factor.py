if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        n = int(input().strip())
        while n % 2 == 0 and n is not 0:
            n >>= 1
        last = 0
        for i in range(3, int(n ** 0.5), 2):
            while n % i == 0 and n > 0:
                last = n
                n = n // i
        print(n if n > 2 else last)
