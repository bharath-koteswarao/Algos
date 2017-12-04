from bisect import bisect_left as bs

if __name__ == '__main__':
    s = input().strip()
    dic = {'Q': [], 'A': []}
    for i in range(len(s)):
        if s[i] == 'Q':
            dic['Q'].append(i)
        elif s[i] == 'A':
            dic['A'].append(i)
    l1 = dic['Q']
    l2 = dic['A']
    ans = 0
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            l, r = l1[i], l1[j]
            ipl = bs(l2, l, 0, len(l2))
            ipr = bs(l2, r, 0, len(l2))
            ans += ipr - ipl
    print(ans)
