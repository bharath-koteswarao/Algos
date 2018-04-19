"""
5
0 0 0 0 2 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0
1 2 2 3 4 0 3 4 4 1 3 1 4 4 1 0 0 0 0 0 4 2 3 2 2 1
1 1 3 3 1 1 4 4 3 1 3 3 3 0 1 2 0 4 2 1 3 0 3 1 1 1
3 3 0 2 2 2 4 1 2 1 1 1 3 3 0 0 3 2 2 4 1 4 4 1 2 1
2 1 4 1 0 2 0 3 1 2 0 3 1 1 2 0 1 4 2 3 2 3 2 0 2 1
"""

"""
1
25
24
25
21
"""

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        l = [int(__) for __ in input().strip().split()]
        l = [__ for __ in l if __ > 0]
        ans = 0
        car, i = 0, 0
        while i < len(l) - 1:
            if l[i] % 2 == 1:
                l[i + 1] += 1
                car = l[i] - 1
                l[i] = 0
            else:
                car = l[i] - 1
                l[i] = 0
            i += 1
            while i < len(l) - 1 and car > 0:
                if l[i] > car:
                    l[i] -= car
                    ans += car
                    car = 0
                else:
                    ans += l[i]
                    car -= l[i]
                    l[i] = 0
                i += 1
        print(ans)
