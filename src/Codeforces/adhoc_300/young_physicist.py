if __name__ == '__main__':
    a, b, c = 0, 0, 0
    for _ in range(int(input().strip())):
        d, e, f = [int(__) for __ in input().strip().split()]
        a += d
        b += e
        c += f
    print("YES" if a == 0 and b == 0 and c == 0 else "NO")