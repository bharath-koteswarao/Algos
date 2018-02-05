if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, m, x, k = [int(i) for i in input().strip().split()]
        st = input().strip()
        e, o = 0, 0
        for i in st:
            if i == 'E':
                e += 1
            else:
                o += 1
        for i in range(1, m + 1):
            if i % 2 == 1:
                if o >= x:
                    n -= x
                    o -= x
                else:
                    n -= o
                    o = 0
            else:
                if e >= x:
                    n -= x
                    e -= x
                else:
                    n -= e
                    e = 0
            if n <= 0:
                break
        print("yes" if n <= 0 else "no")
