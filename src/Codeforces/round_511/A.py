if __name__ == '__main__':
    n = int(input().strip())
    a, b = 1, 2
    c = n - 3
    if c % 3 == 0:
        b -= 1
        c += 1
    print(a, b, c)
