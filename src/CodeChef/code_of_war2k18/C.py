from bisect import bisect_left as bs


def SieveOfEratosthenes(n):
    l = []
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            l.append(p)
    return l


if __name__ == '__main__':
    l = SieveOfEratosthenes(1000004)
    for _ in range(int(input().strip())):
        n = int(input().strip())
        pos = bs(l, n - 0.1)
        print(((2 ** n) - 1) % l[pos])
