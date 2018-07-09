if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    st = input().strip()
    dic = {}
    for i in range(len(st)):
        if st[i] in dic:
            dic[st[i]].append(i)
        else:
            dic[st[i]] = [i]
    keys = sorted(list(dic.keys()))
    for i in keys:
        if k > 0:
            if k > len(dic[i]):
                k -= len(dic[i])
                dic[i] = []
            else:
                dic[i] = dic[i][k:]
                k = 0
    ans = []
    for i in dic:
        ans += dic[i]
    ans.sort()
    for i in ans:
        print(st[i], end="")
