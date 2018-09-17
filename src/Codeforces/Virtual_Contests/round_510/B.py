def get(found, dic, ans):
    if len(found) == 3:
        all.append(ans)
    else:
        for x in dic:
            if len(found.union(set(x))) > len(found):
                get(found.union(set(x)), dic, ans + dic[x])


if __name__ == '__main__':
    n = int(input().strip())
    s = set()
    dic = {}
    all = []
    for _ in range(n):
        a, b = input().strip().split()
        a = int(a)
        b = ''.join(sorted(list(b)))
        if b in dic:
            dic[b] = min(dic[b], a)
        else:
            dic[b] = a
        s = s.union(set(b))
    if len(s) < 3:
        print(-1)
    else:
        get(set(), dic, 0)
        print(min(all))