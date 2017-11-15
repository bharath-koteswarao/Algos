if __name__ == '__main__':
    n = int(input().strip())
    ans = ""
    mi = 10 ** 10
    l = []
    for _ in range(n):
        na, p = input().strip().split(" ")
        a = p.count('4')
        b = p.count('7')
        c = len(p)
        if p.count('4') == p.count('7') != 0 == len(p) // 2:
            l.append((na, int(p)))
    if len(l) == 0:
        print(-1)
    else:
        mi = l[0][1]
        ans = l[0][0]
        for i in range(1,len(l)):
            if l[i][1] < mi:
                ans = l[i][0]
        print(ans)
