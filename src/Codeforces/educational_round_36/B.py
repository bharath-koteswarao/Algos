if __name__ == '__main__':
    n, pos, l, r = [int(i) for i in input().strip().split()]
    if l == 1 and r == n:
        print(0)
    elif l == 1:
        if pos == r:
            print(1)
        elif pos > r:
            print(1 + abs(r - pos))
        elif pos < r:
            print(1 + abs(r - pos))
    elif r == n:
        if pos == l:
            print(1)
        else:
            print(1 + abs(l - pos))
    else:
        if pos == l or pos == r:
            print(2 + r - l)
        elif pos < l:
            print(2 + l - pos + r - l)
        elif pos > r:
            print(2 + pos - r + r - l)
        else:
            x = abs(pos - l)
            y = abs(pos - r)
            print(2 + min(2 * x + y, 2 * y + x))
