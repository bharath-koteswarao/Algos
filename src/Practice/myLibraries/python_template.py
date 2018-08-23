def getPf(n):
    pf = {}
    co = 0
    while n % 2 == 0 and n != 0:
        n //= 2
        co += 1
    if co > 0:
        pf[2] = co
    for i in range(3, int(n ** 0.5) + 1, 2):
        co = 0
        while n % i == 0 and n != 0:
            n //= i
            co += 1
        if co > 0:
            pf[i] = co
    if n > 2:
        pf[n] = 1
    return pf


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    l = []
    for p in range(2, n):
        if prime[p]:
            l.append(p)
    return l
