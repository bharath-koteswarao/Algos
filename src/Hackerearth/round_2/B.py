def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    l = []
    dic = {}
    for p in range(2, n):
        if prime[p]:
            l.append(str(p))
            nn = len(str(p))
            if nn in dic:
                dic[nn] += 1
            else:
                dic[nn] = 1
    return l, dic


if __name__ == '__main__':
    l, dic = SieveOfEratosthenes(10 ** 7)
    l.sort(key=lambda x: len(x))
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(dic[n])
