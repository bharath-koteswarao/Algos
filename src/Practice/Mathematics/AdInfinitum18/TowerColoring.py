if __name__ == '__main__':
    mod = 1000000007
    n = int(input().strip())
    a = 3 ** n
    q = a - (a // (mod - 1)) * (mod - 1)
    while q > mod - 1:
        q = q - (q // (mod - 1)) * (mod - 1)
    print(q)