def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    inp = input().strip()
    i = n - 1
    l = []
    for i in range(n - 1, 0, -1):
        if inp.startswith(inp[i:]):
            l.append(inp[i:])
    if len(l) == 0:
        print(inp * k)
    else:
        ma = ""
        for i in l:
            if len(i) > len(ma):
                ma = i
        ans = inp * 1
        idx = len(ma)
        while occurrences(ans, inp) != k:
            ans += ans[idx]
            idx += 1
        print(ans)
