if __name__ == '__main__':
    a, b, c, d = [int(i) for i in input().strip().split()]
    if 2 * d < c or 2 * c < d or d > 2 * a or d > 2 * b:
        print(-1)
    else:
        print(a)
        print(b)
        print(max(c, d))
