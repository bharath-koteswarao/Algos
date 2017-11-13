from math import factorial as f


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def p(x, y):
    g = gcd(x, y)
    if g == 1:
        print(x)
    else:
        print(str(x // g) + "/" + str(y // g))


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        w = [int(i) for i in input().strip().split(" ")]
        ans = 0
        w = sorted(w)
        fa = f(n)
        if n == 1:
            print(w[0])
        elif n == 2:
            print(sum(w))
        else:
            for i in range(len(w)):
                if i == 0 or i == len(w) - 1:
                    ans += (fa // 3) * w[i]
                else:
                    ans += (fa // 2) * w[i]
        p(ans, fa)
