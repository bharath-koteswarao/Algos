# todo Giving wrong answer make it correct
def comb(n, r, dic):
    r = min(r, n - r)
    if n == r:
        return 1
    elif r == 0:
        return 1
    elif r == 1:
        return n
    elif (n, r) not in dic:
        dic[(n, r)] = comb(n - 1, r, dic) + comb(n - 1, r - 1, dic)
        return dic[(n, r)]
    else:
        return dic[(n, r)]


if __name__ == '__main__':
    mod = 1000000007
    dic = {}
    decomp = {1: 1}
    for i in range(2, 1000):
        n = i
        c = 0
        while n != 1:
            if n in decomp:
                c += decomp[n]
                break
            else:
                c += 1
                n = bin(n)[2:].count('1')
                c += 1 if n == 1 else 0
        decomp[i] = c
    n = input().strip()
    k = int(input().strip())
    l = len(n)
    count = n.count('1')
    ans = 0
    if decomp[count] == k:
        ans += comb(l, count, dic) % mod
    l -= 1
    for i in range(1, len(n)):
        if decomp[i] == k and i != count:
            ans += comb(l, i, dic) % mod
    print(ans)
