from bisect import bisect_left as bs
def SieveOfEratosthenes(n):
    li = []
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            li.append(p)
    return li


if __name__ == '__main__':
    p, y = [int(__) for __ in input().strip().split()]
    li = SieveOfEratosthenes(y)
    # idx = bs(li,p)
    # if li[idx] == p:
    #
