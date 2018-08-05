def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def power(a, n):
    if n == 0:
        return 1
    else:
        r = power(a, n // 2)
        return r * r if n % 2 == 0 else r * r * a


if __name__ == '__main__':
    mod = 1000000007
    for _ in range(int(input().strip())):
        a, b, n = [int(__) for __ in input().strip().split()]
        nc = n
        ac = a
        a *= 2
        while a < abs(a - b) and nc > 1:
            a = a * ac
            nc -= 1
        print(gcd(abs(a - b), a) % mod)
