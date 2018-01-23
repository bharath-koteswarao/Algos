# todo decomp is correct but process in some where wrong
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


def collapse(n):
    ans = 0
    if n == 1:
        return 0
    else:
        while n != 1:
            ans += 1
            n = bin(n)[2:].count('1')
        return ans


if __name__ == '__main__':
    mod = 1000000007
    decomp = {1: 0}
    dic = {}
    for i in range(2, 1001):
        decomp[i] = collapse(i)
    num = input().strip()
    k = int(input().strip())
    ones = num.count('1')
    ans = 0
    l = len(num)
    if decomp[ones] == k:
        ans += comb(l, ones, dic)
    l -= 1
    for i in range(1, l + 1):
        if i != ones:
            if decomp[i] == k:
                ans += comb(l, i, dic) % mod
    print(ans)
    # for i in decomp:
    #     print(decomp[i], end=" ")
