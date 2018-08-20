from math import gcd


def getPf(n):
    li = []
    if n % 2 == 0:
        li.append(2)
        while n % 2 == 0 and n != 0:
            n >>= 1
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0 and n != 0:
            li.append(i)
            while n % i == 0 and n != 0:
                n = n // i
    if n > 2 and n not in li:
        li.append(n)
    return set(li)


def check(x, n):
    for i in range(n):
        if a1[i] % x != 0 and b1[i] % x != 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input().strip())
    a1, b1 = [0 for i in range(n)], [0 for i in range(n)]
    a1[0], b1[0] = [int(__) for __ in input().strip().split()]
    g = gcd(0, a1[0] * b1[0])
    for _ in range(n - 1):
        a1[_ + 1], b1[_ + 1] = [int(__) for __ in input().strip().split()]
        g = gcd(g, a1[_ + 1] * b1[_ + 1])
    pf = getPf(g)
    for x in pf:
        if check(x, n):
            print(x)
            exit(0)
    print(-1)
