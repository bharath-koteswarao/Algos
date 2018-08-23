from math import gcd

if __name__ == '__main__':
    a, b, n = [int(__) for __ in input().strip().split()]
    i = 0
    while True:
        if i % 2 == 0:
            g = gcd(a, n)
            if g > n:
                print(1)
                exit()
            else:
                n -= g
        else:
            g = gcd(b, n)
            if g > n:
                print(0)
                exit()
            else:
                n -= g
        i += 1
