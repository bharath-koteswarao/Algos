def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def mod_exp(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def getPf(n):
    dic = {}
    count = 0
    while n % 2 == 0 and n != 0:
        count += 1
        n >>= 1
    if count > 0:
        dic[2] = count
    for i in range(3, int(n ** 0.5) + 1, 2):
        count = 0
        while n % i == 0 and n != 0:
            n //= i
            count += 1
        if count > 0:
            dic[i] = count
    if n > 2:
        dic[n] = 1
    return dic


if __name__ == '__main__':
    mod = 1000000007
    for _ in range(int(input().strip())):
        a, b, n = [int(__) for __ in input().strip().split()]
        if a - b == 0:
            print((mod_exp(a, n, mod) + mod_exp(b, n, mod)) % mod)
        else:
            pf1 = getPf(a - b)
            pf2 = getPf(b)
            for x in pf2:
                pf2[x] += n - 1
            if 2 in pf2:
                pf2[2] += 1
            else:
                pf2[2] = 1
            ans = 1
            for a in pf1:
                if a in pf2:
                    ans *= mod_exp(a, min(pf1[a], pf2[a]), mod)
            print(ans % mod)
