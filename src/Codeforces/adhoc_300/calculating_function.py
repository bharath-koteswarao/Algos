if __name__ == '__main__':
    n = int(input().strip())
    pos = n // 2 if n % 2 == 0 else (n - 1) // 2
    neg = n if n % 2 == 1 else n - 1
    pos = (pos * (pos + 1))
    neg = ((neg + 1) // 2) ** 2
    print(pos - neg)
