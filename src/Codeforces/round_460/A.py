if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split()]
    l = []
    for _ in range(n):
        a, b = [int(i) for i in input().strip().split()]
        l.append(round(a / b, 11))
    print(min(l) * m)
