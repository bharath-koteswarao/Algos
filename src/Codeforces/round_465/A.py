if __name__ == '__main__':
    n = int(input().strip())
    c = 0
    for i in range(1, n):
        if n % i == 0:
            c += 1
    print(c)
