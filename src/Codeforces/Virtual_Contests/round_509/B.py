from math import gcd

if __name__ == '__main__':
    a, b, x, y = [int(__) for __ in input().strip().split()]
    x //= gcd(x, y)
    y //= gcd(x, y)
    st = 1
    while x * st <= a and y * st <= b:
        st += 1
    print(st - 1)
