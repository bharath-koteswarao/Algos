if __name__ == '__main__':
    n, m, a, b = [int(__) for __ in input().strip().split()]
    if b / m < a:
        print((n // m) * b + min((n % m) * a, b))
    else:
        print(a * n)