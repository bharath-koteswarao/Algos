from statistics import median as med

if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        ar = [int(i) for i in input().strip().split(" ")]
        m = med(ar)
        ans = 0
        for i in ar:
            ans += abs(i - m)
        print(int(ans))
