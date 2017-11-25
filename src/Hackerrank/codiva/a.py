"""
3
2 5
2 2
24 28
"""


# from bisect import bisect_left as bs


def si(n, dic):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            dic[p] = 0
    return dic


if __name__ == '__main__':
    tc = int(input().strip())
    inp = [[] for i in range(tc)]
    for _ in range(tc):
        inp[_] = [int(i) for i in input().strip().split(" ")]
    s, b = inp[0][0], inp[0][1]
    for i in inp:
        s = min(s, min(i))
        b = max(b, max(i))
    primes = si(b + 1, {})
    c = 0
    keys = list(primes.keys())
    # print(keys)
    for t in inp:
        p, q = t[0], t[1]
        if p in primes and q in primes:
            print(q - p)
        elif p in primes and q not in primes:
            while q not in primes and q > p:
                q -= 1
            print(q - p)
        elif p not in primes and q in primes:
            while p not in primes and p < q:
                p += 1
            print(q - p)
        else:
            while p not in primes and p < q:
                p += 1
            while q not in primes and q > p:
                q -= 1
            print(q - p)
