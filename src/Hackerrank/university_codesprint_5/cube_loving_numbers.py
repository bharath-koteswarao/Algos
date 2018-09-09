from math import ceil


def sieve(n):
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


# if __name__ == '__main__':
#     for _ in range(int(input().strip())):
#         n = int(input().strip())
#         ma = int(ceil(n ** (1 / 3)))
#         finished = set()
#         ans = 0
#         for i in range(2, ma + 1):
#             if i not in finished:
#                 ans += (n // i ** 3)
#                 st = 2
#                 while i ** st < ma:
#                     finished.add(i ** st)
#                     st += 1
#         print(ans)

# from math import ceil
#
# if __name__ == '__main__':
#     for _ in range(int(input().strip())):
#         n = int(input().strip())
#         ma = int(ceil(n ** (1 / 3)))
#         se = set()
#         primes = []
#         if ma ** 3 > n:
#             primes = sieve(ma)
#         else:
#             primes = sieve(ma + 1)
#         ans = 0
#         for x in primes:
#             # st = 1
#             # l = []
#             # while (x ** 3) * st <= n:
#             #     cur = (x ** 3) * st
#             #     l.append(cur)
#             #     if cur in se:
#             #         print(x, st, (x ** 3) * st)
#             #         pass
#             #     else:
#             #         se.add(cur)
#             #     st += 1
#             # print(x, len(l), l)
#             ans += n // (x ** 3)
#             for y in primes:
#                 if y == x:
#                     break
#                 else:
#                     ans -= ceil((n // x) / (y ** 3))
#         print(ans)
#         # print(len(se))

#
#
# from math import ceil
#
#
# def sieve(n):
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     l = []
#     for p in range(2, n):
#         if prime[p]:
#             l.append(p)
#     return l
#

# if __name__ == '__main__':
#     for _ in range(int(input().strip())):
#         n = int(input().strip())
#         ma = int(ceil(n ** (1 / 3)))
#         primes = []
#         if ma ** 3 > n:
#             primes = sieve(ma)
#         else:
#             primes = sieve(ma + 1)
#         ans = 0
#         for x in primes:
#             ans += n // (x ** 3)
#         print(ans)


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        ma = int(ceil(n ** (1 / 3)))
        primes = []
        if ma ** 3 > n:
            primes = sieve(ma)
        else:
            primes = sieve(ma + 1)
        ans = 0
        for i in range(len(primes)):
            cur = 0
            st = 1
            p = primes[i] ** 3
            while p * st <= n:
                st += 1
                cur += 1
            ans += cur
            for j in range(i + 1, len(primes)):
                cub = primes[j] ** 3
                re = 0
                st = 1
                while cub * st <= cur:
                    st += 1
                    re += 1
                ans -= re
        print(ans)

"""
6
100
1000
10000
100000
1000000
10000000
"""
