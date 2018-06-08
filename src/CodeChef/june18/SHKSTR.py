def get_pre(s, st):
    curr = 0
    while curr < min(len(s), len(st)) and s[curr] == st[curr]:
        curr += 1
    return curr


if __name__ == '__main__':
    l = []
    for _ in range(int(input().strip())):
        l.append(input().strip())
    ne = []
    cm = l[0]
    for _ in range(len(l)):
        ne.append(min(cm, l[_]))
        cm = min(cm, l[_])
    for _ in range(int(input().strip())):
        lim, s = input().strip().split()
        lim = int(lim)
        ans, ma = "", 0
        for i in range(lim):
            cur = get_pre(s, l[i])
            if cur > ma:
                ma = cur
                ans = l[i]
            elif cur == ma:
                ans = min(ans, l[i])
        print(ans if len(ans) > 0 else ne[lim - 1])
