"""
2
1 10
3 5
"""


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return prime


if __name__ == '__main__':
    tc = int(input().strip())
    m = 0
    test_cases = []
    for _ in range(tc):
        test_cases.append([int(i) for i in input().strip().split(" ")])
        m = max(m, test_cases[_][1])
    primes = SieveOfEratosthenes(m)
    for test_case in test_cases:
        a, b = test_case
        for i in range(a, b + 1):
            if primes[i] and i != 1:
                print(i)
        print()
