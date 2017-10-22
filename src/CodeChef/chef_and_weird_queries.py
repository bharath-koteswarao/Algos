from math import floor as flr

if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        ans = 0
        y = int(input().strip())
        above700 = flr(y ** 0.5) - 700 + 1
        ans += above700 if above700 > 0 else 0
        count = 0
        for i in range(1, y + 1):
            for j in range(i + count, y // i + 1):
                if j ** 0.5 == int(j ** 0.5):
                    print("sol", i, j)
            # print(i, y // i, count)
            count += 1
        print()
