if __name__ == '__main__':
    m, n = [int(__) for __ in input().strip().split()]
    print((m // 2) * n + ((m % 2) * n) // 2)