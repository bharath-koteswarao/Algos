if __name__ == '__main__':
    n,a,b = [int(i) for i in input().strip().split()]
    if n == a + b:
        print(1)
    else:
        l = [(0,0) for i in range(n)]
        l[0] = (1,0)
        a -= 1
        while True:
            for i in range(n):
                if a > 0:
                    if l[i][0] > 0:
                        l[i] = (l[i][0] + 1, 0)
                    else:
                        l[i] = (0, l[i][1] + 1)
                    a -= 1
                el
