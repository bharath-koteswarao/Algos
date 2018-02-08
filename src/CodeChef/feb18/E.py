from fractions import Fraction as Fr
from math import *


def get_acos(x):
    return round(degrees(acos(x)), 2)


if __name__ == '__main__':
    mod = 1000000007
    mmi = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or mmi(n, A % n, t, s - A // n * t, N or n), -1)[n < 1]
    for _ in range(int(input().strip())):
        r, d, t = [int(i) for i in input().strip().split()]
        angle = t * get_acos(Fr(d / r))
        frac = r * Fr(cos(radians(angle))).limit_denominator(1000)
        p = frac.numerator
        q = frac.denominator
        if p < 0:
            p *= -1
            q *= (-1)
        print((p * mmi(q, mod)) % mod)
