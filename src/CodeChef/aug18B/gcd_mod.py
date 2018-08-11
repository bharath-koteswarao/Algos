def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def power(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def fast_exp(x, n):
    result = 1
    partial = x

    for bit in bin(n)[2:]:
        if bit:
            result *= partial
        partial ^= 2

    return result


if __name__ == '__main__':
    mod = 1000000007
    for _ in range(int(input().strip())):
        a, b, n = [int(__) for __ in input().strip().split()]
        if a - b == 0:
            print((power(a, n, mod) + power(b, n, mod)) % mod)
        else:
            temp = b
            b *= 2
            nc = n
            while nc > 1 and b < abs(a - b):
                b *= temp
                nc -= 1
            g = gcd(abs(a - temp), b)
            print(g % mod)
