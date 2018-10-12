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


def check(s):
    for x in s:
        if n - x in s:
            return True
    return False


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        pf = SieveOfEratosthenes(n + 1)
        l = []
        for i in range(len(pf)):
            for j in range(i + 1, len(pf)):
                l.append(pf[i] * pf[j])
        l.sort()
        s = set(l)
        print("YES" if check(s) else "NO")
