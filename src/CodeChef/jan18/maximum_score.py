from bisect import bisect_left as bs

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        l = []
        n = int(input().strip())
        for __ in range(n):
            arr = [int(i) for i in input().strip().split()]
            l.append(sorted(arr))
        l = l[::-1]
        m = max(l[0])
        ans = m
        valid = True
        for i in range(1, n):
            pos = bs(l[i], m - 0.1)
            if pos == 0:
                valid = False
            else:
                m = l[i][pos - 1]
                ans += m
            if not valid:
                break
        print(ans if valid else -1)
