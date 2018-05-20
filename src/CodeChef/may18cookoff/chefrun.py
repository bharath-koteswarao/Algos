if __name__ == '__main__':
    for _ in range(int(input().strip())):
        x1, x2, x3, v1, v2 = [int(__) for __ in input().strip().split()]
        t1 = abs(x1 - x3) / v1
        t2 = abs(x2 - x3) / v2
        if t1 == t2:
            print("Draw")
        elif t1 > t2:
            print("Kefa")
        else:
            print("Chef")
