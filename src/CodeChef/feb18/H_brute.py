if __name__ == '__main__':
    n = int(input().strip())
    l = []
    for i in range(n):
        a, b = [int(p) for p in input().strip().split()]
        l.append((a, b))
    q = int(input().strip())
    for j in range(q):
        arr = [int(i) for i in input().strip().split()]
        ans = 0
        for segment in l:
            count = 0
            for x in arr:
                if segment[0] <= x <= segment[1]:
                    count += 1
            if count % 2 == 1:
                ans += 1
        print(ans)
