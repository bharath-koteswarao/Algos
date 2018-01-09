if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    # m % 2 ** n
    b = bin(m)[2:]
    if n > len(b):
        print(m)
    else:
        print(int(b[len(b) - n:], 2))
