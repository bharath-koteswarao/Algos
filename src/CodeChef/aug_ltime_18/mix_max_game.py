if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, z1, z2 = [int(__) for __ in input().strip().split()]
        a, b = [int(__) for __ in input().strip().split()]
        found = False
        p1 = False
        s1, s2 = 10 ** 10, 10 ** 10
        for i in range(1, z1 + 1):
            for j in range(1, z1 + 1):
                if a * i + b * j == z1:
                    s1 = min(s1, i)
                    s2 = min(s2, j)
                    found = True

        if found and (s1 + s2) % 2 == 1:
            print(1)
        else:
            s1, s2 = 10 ** 10, 10 ** 10
            for i in range(1, z2 + 1):
                for j in range(1, z2 + 1):
                    if a * i + b * j == z2:
                        s1 = min(s1, i)
                        s2 = min(s2, j)
                        found = True
            if found and (s1 + s2) % 2 == 1:
                print(1)
            elif found:
                print(2)
            else:
                print(0)
