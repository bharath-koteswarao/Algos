from math import gcd

if __name__ == '__main__':
    mod = 1000000007
    for _ in range(int(input().strip())):
        a, b, n = [int(__) for __ in input().strip().split()]
        print(gcd((a ** n) + (b ** n), a - b) % mod)