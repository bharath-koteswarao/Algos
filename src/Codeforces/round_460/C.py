def pr():
    for x in visited:
        for y in x:
            print(y, end=" ")
        print()
    print()


if __name__ == '__main__':
    n, m, req = [int(i) for i in input().strip().split()]
    l = []
    matches = []
    visited = [[[False, False] for i in range(m)] for j in range(n)]
    for _ in range(n):
        l.append(list(input().strip()))
    if n == 1 and m == 1 and req == 1:
        print(1)
    else:
        if req == 1:
            ans = 0
            for li in l:
                ans += li.count('.')
            print(ans)
        else:
            for i in range(n):
                for j in range(m):
                    c = 0
                    p = i
                    q = j
                    if l[p][q] == '.':
                        while not visited[p][q][0] and q < m:
                            visited[p][q][0] = True
                            c += 1
                            if q + 1 < m and l[p][q + 1] == '.':
                                q += 1
                            else:
                                break
                        if c > 0:
                            matches.append(c)
                        c = 0
                        p = i
                        q = j
                        while not visited[p][q][1] and p < n:
                            visited[p][q][1] = True
                            c += 1
                            if p + 1 < n and l[p + 1][q] == '.':
                                p += 1
                            else:
                                break
                        if c > 0:
                            matches.append(c)
            ans = 0
            for i in matches:
                if i >= req:
                    ans += i - req + 1
            print(ans)
