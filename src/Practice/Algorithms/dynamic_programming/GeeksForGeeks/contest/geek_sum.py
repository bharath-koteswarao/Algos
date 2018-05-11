def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def print_sum(limit, primes, fib):
    su = 0
    for i in range(2, limit):
        if primes[i]:
            su += fib[i]
    print(su)


if __name__ == '__main__':
    n = int(input().strip())
    els = []
    for _ in range(n):
        els.append(int(input().strip()))
    ma = max(els)
    fib = [0, 1]
    for i in range(ma - 2):
        fib.append(fib[-1] + fib[-2])
    primes = SieveOfEratosthenes(ma)
    for i in els:
        for j in range(i):
            print(fib[j], end=" ")
        print()
        print_sum(i, primes, fib)
