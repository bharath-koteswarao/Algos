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
    tcs = []
    for _ in range(int(input().strip())):
        tcs.append(int(input().strip(), 2))
    ma = max(tcs) + 1
    si = SieveOfEratosthenes(ma)
    for i in tcs:
        if i in si:
            print(si.index(i) + 1)
        else:
            print(-1)
