import math
from collections import Counter as co


def primeFactors(n):
    # Print the number of two's that divide n
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            l.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        l.append(n)
    return l


if __name__ == '__main__':
    n = int(input().strip())
    s1 = input().strip()
    s2 = input().strip()
    c1 = co(s1)
    c2 = co(s2)
    w1, w2 = 0, 0
    p1, p2 = primeFactors(len(s1)), primeFactors(len(s2))
    p1.sort(reverse=True)
    p2.sort(reverse=True)
    for i in set(s1):
        w1 += ord(i) - ord('a') + 1 + c1[i] + (p1[0] if len(p1) == 1 else p1[1])
    for i in set(s2):
        w2 += ord(i) - ord('a') + 1 + c2[i] + (p2[0] if len(p2) == 1 else p2[1])

    print(w1, w2)
