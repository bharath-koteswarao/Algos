from math import gcd

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

if __name__ == '__main__':
    n = int(input().strip())
    if n <= 2:
        print(n)
    elif n == 3:
        print(6)
    elif n == 4:
        print(12)
    else:
        sieve = SieveOfEratosthenes(n + 1)
        l = []
        for prime in sieve:
            st = 1
            while prime ** st <= n:
                st += 1
            l.append(prime ** (st - 1))
        l.sort()
        idx = len(l) - 1
        ans = 1
        count = 2
        while idx >= 0 and count > 0:
            if l[idx] % 2 == 1:
                ans *= l[idx]
                count -= 1
            idx -= 1
        ev = 0
        for x in l:
            if x % 2 == 0:
                ev = x
                break
        if gcd(n, ans) == 1:
            print(ans * n)
        else:
            print(ans * ev)


